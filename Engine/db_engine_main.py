import os
import pickle
import struct
import shutil


class Database:
    # open
    def __init__(self, name: str):
        self.tables = Database.find_and_open_tables(name)
        self.name = name

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
        os.mkdir(f'Databases/{name}')

    def drop_schema(self):
        self.close()
        shutil.rmtree(f'Databases/{self.name}')


class Table:
    # open
    def __init__(self, table_dir: os.DirEntry):
        self.dir = table_dir
        self.table = open(f'{table_dir.path}/{table_dir.name}.datab', mode='rb+')
        self.translator = Translator(f'{table_dir.path}/{table_dir.name}.meta')
        self.current_entry_count = \
            os.stat(f'{table_dir.path}/{table_dir.name}.datab').st_size / self.translator.entry_length

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
        entry_bin = self.translator.to_bin(entry)
        self.table.seek(id_index * self.translator.entry_length)
        self.table.write(entry_bin)
        pass

    @staticmethod
    #    takes list( tuple(<name>, <type>, <length>)) where each inner tuple represents a new column
    def create_table(database_name: str, table_name: str, structure: list):
        os.mkdir(f'Databases/{database_name}/{table_name}')
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


class Translator:
    def __init__(self, meta_path: str):
        # open and read the config
        self.config = Translator.read_config(meta_path)
        self.struct_format_str = self.get_struct_format()
        self.entry_length = struct.calcsize(self.struct_format_str)
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

    def from_bin(self, entry: bytearray):
        unpacked = list(struct.unpack(self.struct_format_str, entry))
        for column_value, i in zip(unpacked, range(len(unpacked))):
            if type(column_value) is not bytes:
                continue
            unpacked[i] = column_value.decode('ascii')
        return unpacked

    def to_bin(self, entry: list):
        if not len(entry) == len(self.config):
            raise InvalidInputError
        for column_value, i in zip(entry, range(len(entry))):
            if type(column_value) is not str:
                continue
            if len(column_value) > self.config[i][2]:
                raise InvalidInputError
            entry[i] = column_value.encode('ascii')
        return struct.pack(self.struct_format_str, *entry)


class InvalidIDError(Exception):
    pass


class InvalidInputError(Exception):
    pass
