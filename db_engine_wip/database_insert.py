import database_core
import re
from datetime import datetime


def insert(database: database_core.Database, values: list):
    errors = list(check_lengths(database, values))
    if not len(errors) == 0:
        return errors
    else:
        # 'a' stands for append
        with open(database.path, 'a', encoding='utf-8') as db_file:
            for value, length in zip(values, database.colons.values()):
                db_file.write(value)
                if type(length) is int:
                    for i in range(length - len(value)):
                        db_file.write('~')
            db_file.close()
        return 'Success!'


def check_lengths(database: database_core.Database, input_list: list):
    if not len(input_list) == len(database.colons):
        print(input_list, len(input_list), len(database.colons))
        yield 'Wrong number of arguments!'
    else:
        for colon, value in zip(database.colons, input_list):
            length_or_type = database.colons.get(colon)
            if length_or_type not in database_core.types_length:
                if len(value) > length_or_type:
                    yield f'Value at {colon} is too long!'
            else:
                if length_or_type == 'date':
                    try:
                        datetime.strptime(value, '%Y-%m-%d')
                    except ValueError:
                        yield ValueError(f'Incorrect data format at {colon}, should be YYYY-MM-DD')
                elif length_or_type == 'gender':
                    if re.fullmatch(r'[mfn]', value):
                        yield f'Incorrect value at {colon}, should be m/f/n'
