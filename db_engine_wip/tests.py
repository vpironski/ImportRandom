from database_core import Database
import database_insert

# test for open (initializing an object of Database is considered opening a database -> __init__ == open
db = Database('Databases/test_db.datab')
keys = db.colons.keys()
# print(db.colons)
# print(db.entry_length)

# tested drop (is working)
# db.drop()
# del db

# input_for_create = {'name': 15, 'family': 15, 'town': 10, 'birth_date': 'date'}
# Database.create(input_for_create)

database_insert.check_lengths(db, ['Georgi', 'Oreshkov', 19303,  'Panagyurishte', 'M', '308', '2005-11-03', 6.00])
