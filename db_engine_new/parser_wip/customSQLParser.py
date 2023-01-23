# Generated from .\customSQL\customSQL.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 32, 150, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 47, 8, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 54, 8, 1, 1,
        2, 1, 2, 1, 2, 5, 2, 59, 8, 2, 10, 2, 12, 2, 62, 9, 2, 1, 3, 1, 3, 1, 4, 1, 4, 1, 5, 1, 5, 1,
        5, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 9, 1, 9, 1, 10, 1, 10, 1, 11, 1, 11,
        1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12, 5, 12,
        98, 8, 12, 10, 12, 12, 12, 101, 9, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 5, 13,
        109, 8, 13, 10, 13, 12, 13, 112, 9, 13, 1, 13, 3, 13, 115, 8, 13, 1, 14, 1, 14, 1, 14,
        1, 14, 1, 15, 1, 15, 1, 15, 1, 15, 3, 15, 125, 8, 15, 1, 16, 1, 16, 1, 16, 1, 16, 1, 16,
        1, 16, 1, 16, 5, 16, 134, 8, 16, 10, 16, 12, 16, 137, 9, 16, 1, 16, 1, 16, 1, 17, 1, 17,
        1, 17, 1, 18, 1, 18, 1, 19, 1, 19, 1, 19, 1, 19, 1, 19, 0, 0, 20, 0, 2, 4, 6, 8, 10, 12, 14,
        16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 0, 4, 1, 0, 17, 22, 1, 0, 2, 7, 1, 0, 11,
        12, 2, 0, 11, 11, 31, 31, 141, 0, 46, 1, 0, 0, 0, 2, 48, 1, 0, 0, 0, 4, 55, 1, 0, 0, 0, 6,
        63, 1, 0, 0, 0, 8, 65, 1, 0, 0, 0, 10, 67, 1, 0, 0, 0, 12, 70, 1, 0, 0, 0, 14, 72, 1, 0, 0,
        0, 16, 77, 1, 0, 0, 0, 18, 79, 1, 0, 0, 0, 20, 81, 1, 0, 0, 0, 22, 83, 1, 0, 0, 0, 24, 94,
        1, 0, 0, 0, 26, 102, 1, 0, 0, 0, 28, 116, 1, 0, 0, 0, 30, 120, 1, 0, 0, 0, 32, 126, 1, 0,
        0, 0, 34, 140, 1, 0, 0, 0, 36, 143, 1, 0, 0, 0, 38, 145, 1, 0, 0, 0, 40, 47, 3, 2, 1, 0, 41,
        47, 3, 22, 11, 0, 42, 47, 3, 26, 13, 0, 43, 47, 3, 30, 15, 0, 44, 47, 3, 32, 16, 0, 45,
        47, 3, 38, 19, 0, 46, 40, 1, 0, 0, 0, 46, 41, 1, 0, 0, 0, 46, 42, 1, 0, 0, 0, 46, 43, 1, 0,
        0, 0, 46, 44, 1, 0, 0, 0, 46, 45, 1, 0, 0, 0, 47, 1, 1, 0, 0, 0, 48, 49, 5, 14, 0, 0, 49, 50,
        3, 4, 2, 0, 50, 51, 5, 15, 0, 0, 51, 53, 3, 8, 4, 0, 52, 54, 3, 10, 5, 0, 53, 52, 1, 0, 0,
        0, 53, 54, 1, 0, 0, 0, 54, 3, 1, 0, 0, 0, 55, 60, 3, 6, 3, 0, 56, 57, 5, 1, 0, 0, 57, 59, 3,
        6, 3, 0, 58, 56, 1, 0, 0, 0, 59, 62, 1, 0, 0, 0, 60, 58, 1, 0, 0, 0, 60, 61, 1, 0, 0, 0, 61,
        5, 1, 0, 0, 0, 62, 60, 1, 0, 0, 0, 63, 64, 5, 10, 0, 0, 64, 7, 1, 0, 0, 0, 65, 66, 5, 10, 0,
        0, 66, 9, 1, 0, 0, 0, 67, 68, 5, 16, 0, 0, 68, 69, 3, 12, 6, 0, 69, 11, 1, 0, 0, 0, 70, 71,
        3, 14, 7, 0, 71, 13, 1, 0, 0, 0, 72, 73, 3, 6, 3, 0, 73, 74, 3, 16, 8, 0, 74, 75, 3, 18, 9,
        0, 75, 76, 3, 20, 10, 0, 76, 15, 1, 0, 0, 0, 77, 78, 7, 0, 0, 0, 78, 17, 1, 0, 0, 0, 79, 80,
        7, 1, 0, 0, 80, 19, 1, 0, 0, 0, 81, 82, 7, 2, 0, 0, 82, 21, 1, 0, 0, 0, 83, 84, 5, 23, 0, 0,
        84, 85, 5, 24, 0, 0, 85, 86, 3, 8, 4, 0, 86, 87, 5, 8, 0, 0, 87, 88, 3, 4, 2, 0, 88, 89, 5,
        9, 0, 0, 89, 90, 5, 25, 0, 0, 90, 91, 5, 8, 0, 0, 91, 92, 3, 24, 12, 0, 92, 93, 5, 9, 0, 0,
        93, 23, 1, 0, 0, 0, 94, 99, 3, 20, 10, 0, 95, 96, 5, 1, 0, 0, 96, 98, 3, 20, 10, 0, 97, 95,
        1, 0, 0, 0, 98, 101, 1, 0, 0, 0, 99, 97, 1, 0, 0, 0, 99, 100, 1, 0, 0, 0, 100, 25, 1, 0, 0,
        0, 101, 99, 1, 0, 0, 0, 102, 103, 5, 26, 0, 0, 103, 104, 3, 8, 4, 0, 104, 105, 5, 27, 0,
        0, 105, 110, 3, 28, 14, 0, 106, 107, 5, 1, 0, 0, 107, 109, 3, 28, 14, 0, 108, 106, 1,
        0, 0, 0, 109, 112, 1, 0, 0, 0, 110, 108, 1, 0, 0, 0, 110, 111, 1, 0, 0, 0, 111, 114, 1,
        0, 0, 0, 112, 110, 1, 0, 0, 0, 113, 115, 3, 10, 5, 0, 114, 113, 1, 0, 0, 0, 114, 115, 1,
        0, 0, 0, 115, 27, 1, 0, 0, 0, 116, 117, 3, 6, 3, 0, 117, 118, 5, 2, 0, 0, 118, 119, 3, 20,
        10, 0, 119, 29, 1, 0, 0, 0, 120, 121, 5, 28, 0, 0, 121, 122, 5, 15, 0, 0, 122, 124, 3,
        8, 4, 0, 123, 125, 3, 10, 5, 0, 124, 123, 1, 0, 0, 0, 124, 125, 1, 0, 0, 0, 125, 31, 1,
        0, 0, 0, 126, 127, 5, 29, 0, 0, 127, 128, 5, 30, 0, 0, 128, 129, 3, 8, 4, 0, 129, 130,
        5, 8, 0, 0, 130, 135, 3, 34, 17, 0, 131, 132, 5, 1, 0, 0, 132, 134, 3, 34, 17, 0, 133,
        131, 1, 0, 0, 0, 134, 137, 1, 0, 0, 0, 135, 133, 1, 0, 0, 0, 135, 136, 1, 0, 0, 0, 136,
        138, 1, 0, 0, 0, 137, 135, 1, 0, 0, 0, 138, 139, 5, 9, 0, 0, 139, 33, 1, 0, 0, 0, 140, 141,
        3, 6, 3, 0, 141, 142, 3, 36, 18, 0, 142, 35, 1, 0, 0, 0, 143, 144, 7, 3, 0, 0, 144, 37,
        1, 0, 0, 0, 145, 146, 5, 32, 0, 0, 146, 147, 5, 30, 0, 0, 147, 148, 3, 8, 4, 0, 148, 39,
        1, 0, 0, 0, 8, 46, 53, 60, 99, 110, 114, 124, 135
    ]


class customSQLParser(Parser):
    grammarFileName = "customSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "','", "'='", "'>'", "'<'", "'>='", "'<='",
                    "'<>'", "'('", "')'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "ID", "INT", "STRING", "WS",
                     "SELECT", "FROM", "WHERE", "EQ", "NE", "GT", "LT",
                     "GE", "LE", "INSERT", "INTO", "VALUES", "UPDATE",
                     "SET", "DELETE", "CREATE", "TABLE", "VARCHAR", "DROP"]

    RULE_statement = 0
    RULE_select_statement = 1
    RULE_columns = 2
    RULE_column = 3
    RULE_table_name = 4
    RULE_where_clause = 5
    RULE_condition = 6
    RULE_comparison_expression = 7
    RULE_comparison = 8
    RULE_operator = 9
    RULE_value = 10
    RULE_insert_statement = 11
    RULE_values = 12
    RULE_update_statement = 13
    RULE_assignment = 14
    RULE_delete_statement = 15
    RULE_create_statement = 16
    RULE_column_def = 17
    RULE_type = 18
    RULE_drop_statement = 19

    ruleNames = ["statement", "select_statement", "columns", "column",
                 "table_name", "where_clause", "condition", "comparison_expression",
                 "comparison", "operator", "value", "insert_statement",
                 "values", "update_statement", "assignment", "delete_statement",
                 "create_statement", "column_def", "type", "drop_statement"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ID = 10
    INT = 11
    STRING = 12
    WS = 13
    SELECT = 14
    FROM = 15
    WHERE = 16
    EQ = 17
    NE = 18
    GT = 19
    LT = 20
    GE = 21
    LE = 22
    INSERT = 23
    INTO = 24
    VALUES = 25
    UPDATE = 26
    SET = 27
    DELETE = 28
    CREATE = 29
    TABLE = 30
    VARCHAR = 31
    DROP = 32

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_statement(self):
            return self.getTypedRuleContext(customSQLParser.Select_statementContext, 0)

        def insert_statement(self):
            return self.getTypedRuleContext(customSQLParser.Insert_statementContext, 0)

        def update_statement(self):
            return self.getTypedRuleContext(customSQLParser.Update_statementContext, 0)

        def delete_statement(self):
            return self.getTypedRuleContext(customSQLParser.Delete_statementContext, 0)

        def create_statement(self):
            return self.getTypedRuleContext(customSQLParser.Create_statementContext, 0)

        def drop_statement(self):
            return self.getTypedRuleContext(customSQLParser.Drop_statementContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement"):
                listener.enterStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement"):
                listener.exitStatement(self)

    def statement(self):

        localctx = customSQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.select_statement()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.insert_statement()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.update_statement()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.delete_statement()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.create_statement()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.drop_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(customSQLParser.SELECT, 0)

        def columns(self):
            return self.getTypedRuleContext(customSQLParser.ColumnsContext, 0)

        def FROM(self):
            return self.getToken(customSQLParser.FROM, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def where_clause(self):
            return self.getTypedRuleContext(customSQLParser.Where_clauseContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_select_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_statement"):
                listener.enterSelect_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_statement"):
                listener.exitSelect_statement(self)

    def select_statement(self):

        localctx = customSQLParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(customSQLParser.SELECT)
            self.state = 49
            self.columns()
            self.state = 50
            self.match(customSQLParser.FROM)
            self.state = 51
            self.table_name()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 16:
                self.state = 52
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(customSQLParser.ColumnContext, i)

        def getRuleIndex(self):
            return customSQLParser.RULE_columns

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterColumns"):
                listener.enterColumns(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitColumns"):
                listener.exitColumns(self)

    def columns(self):

        localctx = customSQLParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columns)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.column()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 1:
                self.state = 56
                self.match(customSQLParser.T__0)
                self.state = 57
                self.column()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(customSQLParser.ID, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_column

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterColumn"):
                listener.enterColumn(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitColumn"):
                listener.exitColumn(self)

    def column(self):

        localctx = customSQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(customSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(customSQLParser.ID, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_table_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTable_name"):
                listener.enterTable_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTable_name"):
                listener.exitTable_name(self)

    def table_name(self):

        localctx = customSQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(customSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(customSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(customSQLParser.ConditionContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_where_clause

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWhere_clause"):
                listener.enterWhere_clause(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWhere_clause"):
                listener.exitWhere_clause(self)

    def where_clause(self):

        localctx = customSQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(customSQLParser.WHERE)
            self.state = 68
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_expression(self):
            return self.getTypedRuleContext(customSQLParser.Comparison_expressionContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_condition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCondition"):
                listener.enterCondition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCondition"):
                listener.exitCondition(self)

    def condition(self):

        localctx = customSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.comparison_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comparison_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(customSQLParser.ColumnContext, 0)

        def comparison(self):
            return self.getTypedRuleContext(customSQLParser.ComparisonContext, 0)

        def operator(self):
            return self.getTypedRuleContext(customSQLParser.OperatorContext, 0)

        def value(self):
            return self.getTypedRuleContext(customSQLParser.ValueContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_comparison_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComparison_expression"):
                listener.enterComparison_expression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComparison_expression"):
                listener.exitComparison_expression(self)

    def comparison_expression(self):

        localctx = customSQLParser.Comparison_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparison_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.column()
            self.state = 73
            self.comparison()
            self.state = 74
            self.operator()
            self.state = 75
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(customSQLParser.EQ, 0)

        def NE(self):
            return self.getToken(customSQLParser.NE, 0)

        def GT(self):
            return self.getToken(customSQLParser.GT, 0)

        def LT(self):
            return self.getToken(customSQLParser.LT, 0)

        def GE(self):
            return self.getToken(customSQLParser.GE, 0)

        def LE(self):
            return self.getToken(customSQLParser.LE, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_comparison

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComparison"):
                listener.enterComparison(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComparison"):
                listener.exitComparison(self)

    def comparison(self):

        localctx = customSQLParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return customSQLParser.RULE_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOperator"):
                listener.enterOperator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOperator"):
                listener.exitOperator(self)

    def operator(self):

        localctx = customSQLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 252) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(customSQLParser.INT, 0)

        def STRING(self):
            return self.getToken(customSQLParser.STRING, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_value

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterValue"):
                listener.enterValue(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitValue"):
                listener.exitValue(self)

    def value(self):

        localctx = customSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not (_la == 11 or _la == 12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Insert_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(customSQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(customSQLParser.INTO, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def columns(self):
            return self.getTypedRuleContext(customSQLParser.ColumnsContext, 0)

        def VALUES(self):
            return self.getToken(customSQLParser.VALUES, 0)

        def values(self):
            return self.getTypedRuleContext(customSQLParser.ValuesContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_insert_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInsert_statement"):
                listener.enterInsert_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInsert_statement"):
                listener.exitInsert_statement(self)

    def insert_statement(self):

        localctx = customSQLParser.Insert_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_insert_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(customSQLParser.INSERT)
            self.state = 84
            self.match(customSQLParser.INTO)
            self.state = 85
            self.table_name()
            self.state = 86
            self.match(customSQLParser.T__7)
            self.state = 87
            self.columns()
            self.state = 88
            self.match(customSQLParser.T__8)
            self.state = 89
            self.match(customSQLParser.VALUES)
            self.state = 90
            self.match(customSQLParser.T__7)
            self.state = 91
            self.values()
            self.state = 92
            self.match(customSQLParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(customSQLParser.ValueContext, i)

        def getRuleIndex(self):
            return customSQLParser.RULE_values

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterValues"):
                listener.enterValues(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitValues"):
                listener.exitValues(self)

    def values(self):

        localctx = customSQLParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_values)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.value()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 1:
                self.state = 95
                self.match(customSQLParser.T__0)
                self.state = 96
                self.value()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Update_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(customSQLParser.UPDATE, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def SET(self):
            return self.getToken(customSQLParser.SET, 0)

        def assignment(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(customSQLParser.AssignmentContext, i)

        def where_clause(self):
            return self.getTypedRuleContext(customSQLParser.Where_clauseContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_update_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUpdate_statement"):
                listener.enterUpdate_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUpdate_statement"):
                listener.exitUpdate_statement(self)

    def update_statement(self):

        localctx = customSQLParser.Update_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_update_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(customSQLParser.UPDATE)
            self.state = 103
            self.table_name()
            self.state = 104
            self.match(customSQLParser.SET)
            self.state = 105
            self.assignment()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 1:
                self.state = 106
                self.match(customSQLParser.T__0)
                self.state = 107
                self.assignment()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 16:
                self.state = 113
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(customSQLParser.ColumnContext, 0)

        def value(self):
            return self.getTypedRuleContext(customSQLParser.ValueContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_assignment

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAssignment"):
                listener.enterAssignment(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAssignment"):
                listener.exitAssignment(self)

    def assignment(self):

        localctx = customSQLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.column()
            self.state = 117
            self.match(customSQLParser.T__1)
            self.state = 118
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Delete_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(customSQLParser.DELETE, 0)

        def FROM(self):
            return self.getToken(customSQLParser.FROM, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def where_clause(self):
            return self.getTypedRuleContext(customSQLParser.Where_clauseContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_delete_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDelete_statement"):
                listener.enterDelete_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDelete_statement"):
                listener.exitDelete_statement(self)

    def delete_statement(self):

        localctx = customSQLParser.Delete_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_delete_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(customSQLParser.DELETE)
            self.state = 121
            self.match(customSQLParser.FROM)
            self.state = 122
            self.table_name()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 16:
                self.state = 123
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(customSQLParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(customSQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def column_def(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.Column_defContext)
            else:
                return self.getTypedRuleContext(customSQLParser.Column_defContext, i)

        def getRuleIndex(self):
            return customSQLParser.RULE_create_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCreate_statement"):
                listener.enterCreate_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCreate_statement"):
                listener.exitCreate_statement(self)

    def create_statement(self):

        localctx = customSQLParser.Create_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_create_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(customSQLParser.CREATE)
            self.state = 127
            self.match(customSQLParser.TABLE)
            self.state = 128
            self.table_name()
            self.state = 129
            self.match(customSQLParser.T__7)
            self.state = 130
            self.column_def()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 1:
                self.state = 131
                self.match(customSQLParser.T__0)
                self.state = 132
                self.column_def()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(customSQLParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(customSQLParser.ColumnContext, 0)

        def type_(self):
            return self.getTypedRuleContext(customSQLParser.TypeContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_column_def

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterColumn_def"):
                listener.enterColumn_def(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitColumn_def"):
                listener.exitColumn_def(self)

    def column_def(self):

        localctx = customSQLParser.Column_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_column_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.column()
            self.state = 141
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(customSQLParser.INT, 0)

        def VARCHAR(self):
            return self.getToken(customSQLParser.VARCHAR, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType"):
                listener.enterType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType"):
                listener.exitType(self)

    def type_(self):

        localctx = customSQLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not (_la == 11 or _la == 31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Drop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(customSQLParser.DROP, 0)

        def TABLE(self):
            return self.getToken(customSQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_drop_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDrop_statement"):
                listener.enterDrop_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDrop_statement"):
                listener.exitDrop_statement(self)

    def drop_statement(self):

        localctx = customSQLParser.Drop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_drop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(customSQLParser.DROP)
            self.state = 146
            self.match(customSQLParser.TABLE)
            self.state = 147
            self.table_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
