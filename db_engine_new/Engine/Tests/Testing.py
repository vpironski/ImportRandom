import db_engine_new.Engine.Main.db_engine_main as eng

"""
missing:
shrink, regex search (like)

"""

# database1 = eng.Database('test')
# util.linear_select(database1.tables['test_table01'])

db = eng.Database('generated')

# count
# print(db.tables['worker'].current_entry_count)

# create, delete
# eng.Database.create('test1')
# db.drop_schema()
#  table creates & inserts are in generate

columns = ['id', 'first_name', 'last_name', 'salary']
for worker in db.linear_select('worker',
                               start=0,
                               # limit=10000,
                               columns=columns,
                               condition=''):
    print(worker)
    pass
