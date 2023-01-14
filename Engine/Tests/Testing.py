import os

import Engine.db_engine_main as eng

table_structure = [('first_name', 's', 5), ('age', 'h', 1)]

os.chdir('..')
# eng.Database.create('test')
# eng.Table.create_table('test', 'test_table01', table_structure)
database1 = eng.Database('test')
# print(database1.tables['test_table01'].current_entry_count)
# entry_a = b'\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x00\x00\x00\x00\x00\x00gamer'
entry_b = [100, 0, 'gamer', 16]      # limit is 32 767
# translated_entry_b = database1.tables.get('test_table01').translator.to_bin(entry_b)
# print(translated_entry_b, type(translated_entry_b))
database1.tables['test_table01'].write(0, entry_b)
print(database1.tables['test_table01'].read(0))
print(database1.tables['test_table01'].current_entry_count)

# try except block for translator usage
# try:
#     print(database1.tables['test_table01'].translator.from_bin(1234567))
# except TypeError:
#     print('wrong datatypes')
