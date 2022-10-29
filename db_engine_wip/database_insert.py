import database_core


def insert(database: database_core.Database):
    # 'a' stands for append
    with open(database.path, 'a', encoding='utf-8') as db_file:

        db_file.close()
