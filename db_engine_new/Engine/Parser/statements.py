from db_engine_new.Engine.Main.db_engine_main import Database
class Statement:
    def execute(self):
        pass


class UseStatement(Statement):
    def __init__(self, schema_name: str):
        self.schema_name = schema_name

    def execute(self):
        return Database(self.schema_name)

