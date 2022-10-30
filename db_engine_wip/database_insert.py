import database_core


def insert(database: database_core.Database):

    # 'a' stands for append
    with open(database.path, 'a', encoding='utf-8') as db_file:

        db_file.close()


def check_lengths(database: database_core.Database, values: list):
    if not len(values) == len(database.colons):
        # print('fail!')
        return False

    index = 0
    for colon in database.colons:

        index += 1
        pass
