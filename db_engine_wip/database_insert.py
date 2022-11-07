import re
import os
from datetime import datetime

import database_core


def insert(database: database_core.Database, values: list):
    errors = list(check_lengths(database, values))
    if not len(errors) == 0:
        return errors
    else:
        database.entry_count += 1
        values.insert(0, str(database.entry_count).zfill(5))
        values.insert(1, '1')
        for value, length in zip(values, database.colons.values()):
            database.db_file.write(value)
            if type(length) is int:
                database.db_file.write((int(length) - len(value)) * '~')
            else:
                database.db_file.write(length)
        database.db_file.flush()
        os.fsync(database.db_file.fileno())


def check_lengths(database: database_core.Database, input_list: list):
    if not len(input_list) == len(database.colons) - 2:
        yield 'Wrong number of arguments!'
    else:
        for colon, value in zip(list(database.colons.keys())[2:], input_list):
            length_or_type = database.colons.get(colon)
            if length_or_type not in database_core.types_length:
                if len(value) > length_or_type:
                    yield f'Value at {colon} is too long!'
            else:
                if length_or_type == 'date':
                    try:
                        datetime.strptime(value, '%Y-%m-%d')
                    except ValueError:
                        yield ValueError(f'Incorrect data format at \'{colon}\', should be YYYY-MM-DD')
                elif length_or_type == 'gender':
                    if not re.fullmatch(r'[mfn]', value):
                        yield f'Incorrect value at \'{colon}\', should be m/f/n'
                elif length_or_type == 'course_number':
                    if not re.fullmatch(r'[0-9]{5}', value):
                        yield f'Incorrect value at \'{colon}\', course number should be exactly 5 digits long'
