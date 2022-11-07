from database_core import Database
import database_select
import os

os.chdir('..')
db = Database('Databases/generated.datab')
ids = database_select.select(db, {
    'name': 'Geralt',
    'gender': 'm',
    'birth_date': '19..-..-24'
})
print(ids)
for i in ids:
    print(database_select.read_entry(db, i))
