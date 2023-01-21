from db_engine.database_core import Database
from db_engine import database_select
import os

os.chdir('..')
db = Database('Databases/generated.datab')
# database_utils.delete(db, 2136)

ids = database_select.select(db, {
    'birth_date': '1889.*',
    'name': 'Adolf',
    'surname': 'Hitler'
})

# # database_utils.delete(db, 2)
# # database_utils.delete(db, 3)
#
# # ids = database_select.select(db)
print(ids)
print(len(ids))
for i in ids:
    print(database_select.read_entry(db, i))

# database_utils.update(db, {'surname': 'Ivanov', 'birth_date': '2009-09-01'}, 0)

# print(db.colons_types)
db.close()
