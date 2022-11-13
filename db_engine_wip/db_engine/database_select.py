from db_engine import database_core
from db_engine.database_core import Database
import re


def select(database: Database, filters=None):
    active_value_index = database_core.id_digits

    for id_num in range(0, database.entry_count):
        entry_str = read_entry(database, id_num)
        if entry_str[active_value_index] == '1':
            entry_dict = get_dict(database, entry_str)
            if filters is not None:
                match = True
                for filter_name in filters:
                    if not re.fullmatch(filters.get(filter_name), entry_dict.get(filter_name)):
                        match = False
                        break
                if match:
                    yield id_num
            else:
                yield id_num


def read_entry(database: Database, id_num):
    position = database.get_entry_position(id_num)
    database.db_file.seek(position)
    return database.db_file.read(database.entry_length)


def get_dict(database: Database, entry):
    dictionary = dict()
    for colon, length in zip(database.colons_types.keys(), database.colons_types.values()):
        if type(length) is not int:
            length = database_core.types_length.get(length)
        dictionary.update({colon: entry[:length].strip('~')})
        entry = entry[length:]
    return dictionary
