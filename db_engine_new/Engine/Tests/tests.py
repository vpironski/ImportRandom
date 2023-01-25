import db_engine_new.Engine.Main.db_engine_main as eng

db = eng.Database('generated')
print(db.tables['worker'].translator.config, '\n', db.tables['worker'].get_structure_info())