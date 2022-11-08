from database_core import Database
import database_select
import os

os.chdir('..')
db = Database('Databases/generated.datab')
ids = database_select.select(db, {
    'birth_date': '.*',
    'name': 'Adolf',
    'surname': 'Hitler'
})
print(ids)
print(len(ids))
for i in ids:
    print(database_select.read_entry(db, i))
