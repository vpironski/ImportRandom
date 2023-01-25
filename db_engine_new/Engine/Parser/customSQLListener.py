from antlr4 import ParseTreeListener

from db_engine_new.Engine.Parser.customSQLParser import customSQLParser
class customSQLListener(ParseTreeListener):

    # Enter a parse tree produced by customSQLParser#statement.
    def enterStatement(self, ctx: customSQLParser.StatementContext):

        pass

    # Exit a parse tree produced by customSQLParser#statement.
    def exitStatement(self, ctx: customSQLParser.StatementContext):
        pass

    # Enter a parse tree produced by customSQLParser#use_statement.
    def enterUse_statement(self, ctx: customSQLParser.Use_statementContext):

        pass

    # Exit a parse tree produced by customSQLParser#use_statement.
    def exitUse_statement(self, ctx: customSQLParser.Use_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#schema_name.
    def enterSchema_name(self, ctx: customSQLParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by customSQLParser#schema_name.
    def exitSchema_name(self, ctx: customSQLParser.Schema_nameContext):
        pass

    # Enter a parse tree produced by customSQLParser#select_statement.
    def enterSelect_statement(self, ctx: customSQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#select_statement.
    def exitSelect_statement(self, ctx: customSQLParser.Select_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#columns.
    def enterColumns(self, ctx: customSQLParser.ColumnsContext):
        # print(ctx.getText())
        pass

    # Exit a parse tree produced by customSQLParser#columns.
    def exitColumns(self, ctx: customSQLParser.ColumnsContext):
        pass

    # Enter a parse tree produced by customSQLParser#column.
    def enterColumn(self, ctx: customSQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by customSQLParser#column.
    def exitColumn(self, ctx: customSQLParser.ColumnContext):
        pass

    # Enter a parse tree produced by customSQLParser#table_name.
    def enterTable_name(self, ctx: customSQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by customSQLParser#table_name.
    def exitTable_name(self, ctx: customSQLParser.Table_nameContext):
        pass

    # Enter a parse tree produced by customSQLParser#where_clause.
    def enterWhere_clause(self, ctx: customSQLParser.Where_clauseContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by customSQLParser#where_clause.
    def exitWhere_clause(self, ctx: customSQLParser.Where_clauseContext):
        pass

    # Enter a parse tree produced by customSQLParser#condition.
    def enterCondition(self, ctx: customSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by customSQLParser#condition.
    def exitCondition(self, ctx: customSQLParser.ConditionContext):
        pass

    # Enter a parse tree produced by customSQLParser#operator.
    def enterOperator(self, ctx: customSQLParser.OperatorContext):
        pass

    # Exit a parse tree produced by customSQLParser#operator.
    def exitOperator(self, ctx: customSQLParser.OperatorContext):
        pass

    # Enter a parse tree produced by customSQLParser#value.
    def enterValue(self, ctx: customSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by customSQLParser#value.
    def exitValue(self, ctx: customSQLParser.ValueContext):
        pass

    # Enter a parse tree produced by customSQLParser#insert_statement.
    def enterInsert_statement(self, ctx: customSQLParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#insert_statement.
    def exitInsert_statement(self, ctx: customSQLParser.Insert_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#values.
    def enterValues(self, ctx: customSQLParser.ValuesContext):
        pass

    # Exit a parse tree produced by customSQLParser#values.
    def exitValues(self, ctx: customSQLParser.ValuesContext):
        pass

    # Enter a parse tree produced by customSQLParser#update_statement.
    def enterUpdate_statement(self, ctx: customSQLParser.Update_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#update_statement.
    def exitUpdate_statement(self, ctx: customSQLParser.Update_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#assignment.
    def enterAssignment(self, ctx: customSQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by customSQLParser#assignment.
    def exitAssignment(self, ctx: customSQLParser.AssignmentContext):
        pass

    # Enter a parse tree produced by customSQLParser#delete_statement.
    def enterDelete_statement(self, ctx: customSQLParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#delete_statement.
    def exitDelete_statement(self, ctx: customSQLParser.Delete_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#create_statement.
    def enterCreate_statement(self, ctx: customSQLParser.Create_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#create_statement.
    def exitCreate_statement(self, ctx: customSQLParser.Create_statementContext):
        pass

    # Enter a parse tree produced by customSQLParser#column_def.
    def enterColumn_def(self, ctx: customSQLParser.Column_defContext):
        pass

    # Exit a parse tree produced by customSQLParser#column_def.
    def exitColumn_def(self, ctx: customSQLParser.Column_defContext):
        pass

    # Enter a parse tree produced by customSQLParser#type.
    def enterType(self, ctx: customSQLParser.TypeContext):
        pass

    # Exit a parse tree produced by customSQLParser#type.
    def exitType(self, ctx: customSQLParser.TypeContext):
        pass

    # Enter a parse tree produced by customSQLParser#drop_statement.
    def enterDrop_statement(self, ctx: customSQLParser.Drop_statementContext):
        pass

    # Exit a parse tree produced by customSQLParser#drop_statement.
    def exitDrop_statement(self, ctx: customSQLParser.Drop_statementContext):
        pass

