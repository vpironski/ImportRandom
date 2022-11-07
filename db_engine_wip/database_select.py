from database_core import Database
import database_core
import re


def select(database: Database, filters=None):
    if filters is None:
        return list(range(0, database.entry_count - 1))
    active_value_index = database_core.id_digits

    new_ids = []
    for id_num in range(0, database.entry_count - 1):
        entry_str = read_entry(database, id_num)
        if entry_str[active_value_index] == '1':
            entry_dict = get_dict(database, entry_str)
            match = True
            for filter_name in filters:
                if not re.fullmatch(filters.get(filter_name), entry_dict.get(filter_name)):
                    match = False
                    break
            if match:
                new_ids.append(id_num)
    return new_ids


def read_entry(database: Database, id_value):
    position = database.get_entry_position(id_value)
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
