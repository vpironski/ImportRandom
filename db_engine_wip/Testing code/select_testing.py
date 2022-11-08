from database_core import Database
import database_select
import database_utils
import os

os.chdir('..')
db = Database('Databases/generated.datab')
# ids = database_select.select(db, {
#     'birth_date': '.*',
#     'name': 'A.*',
#     'surname': '.*'
# })
database_utils.delete(db, 1)
database_utils.delete(db, 2)
database_utils.delete(db, 3)

ids = database_select.select(db)
print(ids)
print(len(ids))
# for i in ids:
#     print(database_select.read_entry(db, i))

# database_utils.update(db, {'surname': 'Petrov', 'birth_date': '2000-01-01'}, 0)

db.close()
