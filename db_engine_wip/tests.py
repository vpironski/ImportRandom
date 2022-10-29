from database_core import Database
import database_insert

# db = Database('Databases/test_db.txt')
# print(db.colons)
# print(db.entry_length)

# tested drop (is working)
# db.drop()
# del db

input_for_create = {'name': 15, 'family': 15, 'town': 10, 'birth_date': 'date'}
db = "Databases/test_db.txt"
Database.create(input_for_create,db)