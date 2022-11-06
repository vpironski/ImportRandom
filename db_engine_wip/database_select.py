from database_core import Database
import re


def select(database: Database, id_list=None, filters: dict = None, max_entries=None):
    if id_list is None:
        if max_entries is not None:
            id_list = zip(range(0, database.entry_count), range(0, max_entries))
        else:
            id_list = range(0, database.entry_count)

    for id_num in id_list:
        positions = database.get_entry_position(id_num)
        database.db_file.seek(positions[0])
        entry_str = database.db_file.read(positions[1])
        print(entry_str)
