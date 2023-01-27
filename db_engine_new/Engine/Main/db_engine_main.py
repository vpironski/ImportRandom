import os
import pickle
import struct
import shutil
import Engine.Main.db_utils as util
from Engine.Main.db_utils import *


class Database:
    # open
    def __init__(self, name: str):
        self.tables: dict = Database.find_and_open_tables(name)
        self.name: str = name

    def close(self):
        for table in self.tables.values():
            table.close()

    @staticmethod
    def find_and_open_tables(database_name: str):
        table_dict = dict()
        tables = os.scandir(f'Databases/{database_name}/')
        if not tables:
            return
        for table_dir in tables:
            if not table_dir.is_dir():
                continue
            table_dict = {table_dir.name: Table(table_dir)}
        return table_dict

    @staticmethod
    def create(name: str):
        if not validate_name(name):
            raise CreationError(
                f'{name} is not a valid Database name. Names should contain upper and lower case letters and `_`')
        try:
            os.mkdir(f'Databases/{name}')
        except FileExistsError:
            raise CreationError(f'Database `{name}` already exists')

    def create_table(self, name: str, structure: list):
        if not validate_name(name):
            raise CreationError(
                f'{name} is not a valid table name. Names should contain upper and lower case letters and `_`')
        Table.create_table(self.name, name, structure)
        self.tables: dict = Database.find_and_open_tables(self.name)

    def drop_schema(self):
        self.close()
        shutil.rmtree(f'Databases/{self.name}')

    def insert(self, table_name: str, entry: list):
        if table_name not in self.tables:
            raise InvalidTableError(f'Table with name `{table_name}` was not found')
        table = self.tables.get(table_name)
        entry = [table.current_entry_count, 0] + entry
        table.write(table.current_entry_count, entry)
        table.current_entry_count += 1

    # entry_updates has the structure: dict({column_name: <new_value>}.....)
    # the only columns that can't be updated are id & inf
    def update(self, table_name: str, id_index: int, entry_updates: dict):
        if table_name not in self.tables:
            raise InvalidTableError(f'Table with name `{table_name}` was not found')
        table = self.tables.get(table_name)
        current_entry = table.get_labeled_entry(table.read(id_index))
        current_entry.update(entry_updates)
        table.write(id_index, list(current_entry.values()))

    def delete(self, table_name: str, id_index: int):
        self.update(table_name, id_index, {'inf': -1})

    def linear_select(self, table_name: str, columns: list = None, start: int = None, limit: int = None,
                      condition: str = None):
        if table_name not in self.tables:
            raise InvalidTableError(f'Table with name `{table_name}` was not found')
        table = self.tables[table_name]

        # check if columns is valid / None
        if columns is None:
            columns = [tup[0] for tup in list(table.translator.config)]
            del columns[1]
            # columns = range(2, len(table.translator.config))

        if start is None:
            start = 0

        # check if there is a limit and if limit is < entry_count
        if limit <= 0 or limit > table.current_entry_count or limit is None:
            limit = table.current_entry_count

        # check if there is a condition and call where
        def condition_check(entry):
            return True

        if condition is not None:
            def condition_check(entry): return where(table, condition, entry)

        for id_index in range(start, limit):
            # read entry
            current_entry = table.read(id_index)
            # validate all conditions ( + not deleted)
            if current_entry[1] < 0:
                continue
            # problem here
            boolean = condition_check(current_entry)
            if not boolean:
                continue
            # process entry according to columns
            current_entry = cut_entry_to(table.get_labeled_entry(current_entry), columns)
            yield current_entry
        pass


class Table:
    # open
    def __init__(self, table_dir: os.DirEntry):
        self.dir: os.DirEntry = table_dir
        self.name = table_dir.name
        self.table = open(f'{table_dir.path}/{table_dir.name}.datab', mode='rb+')
        self.translator = Translator(f'{table_dir.path}/{table_dir.name}.meta')
        self.current_entry_count: int = int(
            os.stat(f'{table_dir.path}/{table_dir.name}.datab').st_size / self.translator.entry_length)

        # must add the index files here to be used by a database_utils.py module
        pass

    def close(self):
        self.table.close()
        # probably more cleanup needed
        pass

    def read(self, id_index: int):
        if id_index > self.current_entry_count or id_index < 0:
            raise InvalidIDError
        self.table.seek(id_index * self.translator.entry_length)
        entry = self.table.read(self.translator.entry_length)
        return self.translator.from_bin(bytearray(entry))
        pass

    def write(self, id_index: int, entry: list):
        if id_index > self.current_entry_count or id_index < 0:
            raise InvalidIDError
        if not len(entry) == len(self.translator.config):
            raise InvalidSyntaxError('Invalid entry length.')

        entry_bin = self.translator.to_bin(entry)
        self.table.seek(id_index * self.translator.entry_length)
        self.table.write(entry_bin)
        pass

    def get_labeled_entry(self, entry: list):
        labeled = dict()
        for column_name, column_value in zip([column[0] for column in self.translator.config], entry):
            labeled[column_name] = column_value
        return labeled

    @staticmethod
    #    takes list( tuple(<name>, <type>, <length>)) where each inner tuple represents a new column
    def create_table(database_name: str, table_name: str, structure: list):
        try:
            os.mkdir(f'Databases/{database_name}/{table_name}')
        except FileExistsError:
            raise CreationError(f'Database `{database_name}.{table_name}` already exists')
        for column_tuple in structure:
            if not validate_name(column_tuple[0]):
                raise CreationError(f'Invalid column name at {column_tuple}, {column_tuple[0]}')
            if not column_tuple[1] in util.data_types.keys():
                raise CreationError(f'Invalid datatype at {column_tuple}, {column_tuple[1]}')
            if not column_tuple[2] >= 0:
                raise CreationError(f'Invalid column length at {column_tuple}, {column_tuple[2]}')

        with open(f'Databases/{database_name}/{table_name}/{table_name}.meta', mode='wb') as meta:
            structure = [('id', 'Q', 1), ('inf', 'q', 1)] + structure
            structure = tuple(structure)
            pickler = pickle.Pickler(meta, protocol=pickle.HIGHEST_PROTOCOL)
            pickler.dump(structure)
        with open(f'Databases/{database_name}/{table_name}/{table_name}.datab', mode='xb'):
            pass

    def drop_table(self):
        self.close()
        shutil.rmtree(self.dir)

    def get_structure_info(self):

        info = list(self.translator.config)
        del info[1]
        for i, column in enumerate(info):
            column = list(column)
            column[1] = util.data_types_descriptive.get(column[1])
            info[i] = column
        return info

    def get_column_names(self):
        return [a[0] for a in self.translator.config]

    def get_functional_column_names(self):
        names = self.get_column_names()
        del names[0]
        del names[0]
        return names


class Translator:
    def __init__(self, meta_path: str):
        # open and read the config
        self.config: tuple = Translator.read_config(meta_path)
        self.struct_format_str: str = self.get_struct_format()
        self.entry_length: int = struct.calcsize(self.struct_format_str)
        pass

    @staticmethod
    def read_config(meta_path: str):
        with open(meta_path, mode='rb') as meta:
            unpickler = pickle.Unpickler(meta)
            return unpickler.load()

    def get_struct_format(self):
        str_format = '>'
        for column in self.config:
            str_format += str(column[2]) + column[1]
        return str_format

    def validate_entry_types(self, raw_entry: list):
        datatypes = [util.data_types.get(a[1]) for a in self.config]
        values = list()
        for column, datatype in zip(raw_entry, datatypes):
            try:
                if datatype == int:
                    values.append(int(column))
                elif datatype == float:
                    values.append(float(column))
                elif datatype == bool:
                    if column.lower() in ("true", "false"):
                        values.append(column.lower() == "true")
                    else:
                        raise InvalidSyntaxError("Invalid value for boolean")
                else:
                    values.append(column)
            except ValueError as e:
                raise InvalidSyntaxError(f"Error casting value '{column}' to {datatype}: {e}")
        pass
        return values

    def from_bin(self, entry: bytearray):
        unpacked = list(struct.unpack(self.struct_format_str, entry))
        for column_value, i in zip(unpacked, range(len(unpacked))):
            if type(column_value) is not bytes:
                continue
            unpacked[i] = column_value.decode('ascii').replace('\x00', '')

        return unpacked

    def to_bin(self, entry: list):
        entry = self.validate_entry_types(entry)
        for column_value, i in zip(entry, range(len(entry))):
            if type(column_value) is not str:
                continue
            if len(column_value) > self.config[i][2]:
                raise InvalidSyntaxError(
                    f'The value given for #{i} is {len(column_value)} bytes long, should be at most {self.config[i][2]}')
            entry[i] = column_value.encode('ascii')
        return struct.pack(self.struct_format_str, *entry)


"""
example of where statement structure
where (<column_name> [=, >, <, >=, <=, =/ not =, in/ not in, between/ not between, like] <value>)+
col1 > 100 and col2 = 10
"""


def where(table: Table, statement: str, entry: list):
    lambda_from_statement = parse_statement(table, statement)
    return eval(lambda_from_statement)(*entry)
    # return boolean
    pass


def parse_statement(table: Table, statement: str):
    name = r'([a-zA-Z][a-zA-Z0-9]*(?:_[a-zA-Z][a-zA-Z0-9]*)*)'
    operator = r'(==|>|<|>=|<=|!=|in|not\sin|like)'
    value = r'(\S+)'
    singular_statement = r'(?:' + name + r'\s' + operator + r'\s' + value + r')'
    divisor = r'(and|or)'
    full_statement = re.compile(r'^' + singular_statement + r'(?:\s' + divisor + r'\s' + singular_statement + r')*$')

    if not full_statement.fullmatch(statement):
        raise InvalidSyntaxError(f'The statement `{statement}` is invalid.')

    like_operator = r'like\s(\'\S+\')'
    like_matches = re.compile(name + r'\s' + like_operator).findall(statement)
    if like_matches:
        for match in like_matches:
            statement = statement.replace(f'{match[0]} like {match[1]}', f'like({match[0]}, {match[1]})')

    match = re.compile(name + r'\s(=|>|<|>=|<=|!=|in|not\sin)\s(\S+)') \
        .findall(statement)
    for columns in match:
        if columns[0] not in [column[0] for column in table.translator.config]:
            raise InvalidSyntaxError(f'Column {columns[0]} not found.')

    lambda_from_statement = 'lambda '
    for a in table.translator.config:
        lambda_from_statement += a[0] + ', '
    return lambda_from_statement.strip(', ') + ': ' + statement
