# Generated from .\parser_wip\customSQL.g4 by ANTLR 4.11.1
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
        4, 1, 46, 195, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 49, 8, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1,
        3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 62, 8, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 5, 4, 69, 8, 4, 10, 4,
        12, 4, 72, 9, 4, 1, 4, 3, 4, 75, 8, 4, 1, 5, 1, 5, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 7, 5, 7, 85,
        8, 7, 10, 7, 12, 7, 88, 9, 7, 1, 8, 1, 8, 1, 8, 1, 8, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9,
        3, 9, 101, 8, 9, 1, 9, 1, 9, 3, 9, 105, 8, 9, 1, 9, 3, 9, 108, 8, 9, 1, 10, 1, 10, 1, 11, 1,
        11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12, 5,
        12, 126, 8, 12, 10, 12, 12, 12, 129, 9, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 5,
        13, 137, 8, 13, 10, 13, 12, 13, 140, 9, 13, 1, 13, 3, 13, 143, 8, 13, 1, 13, 1, 13, 1,
        14, 1, 14, 1, 14, 1, 14, 1, 15, 1, 15, 1, 15, 3, 15, 154, 8, 15, 1, 15, 1, 15, 1, 16, 1,
        16, 1, 16, 1, 16, 1, 16, 1, 16, 1, 16, 5, 16, 165, 8, 16, 10, 16, 12, 16, 168, 9, 16, 1,
        16, 1, 16, 1, 16, 1, 17, 1, 17, 1, 17, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1,
        18, 1, 18, 1, 18, 1, 18, 1, 18, 3, 18, 188, 8, 18, 1, 19, 1, 19, 1, 19, 1, 19, 1, 19, 1,
        19, 0, 0, 20, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
        0, 3, 1, 0, 7, 8, 1, 0, 39, 42, 1, 0, 26, 27, 207, 0, 48, 1, 0, 0, 0, 2, 50, 1, 0, 0, 0, 4,
        54, 1, 0, 0, 0, 6, 56, 1, 0, 0, 0, 8, 74, 1, 0, 0, 0, 10, 76, 1, 0, 0, 0, 12, 78, 1, 0, 0, 0,
        14, 80, 1, 0, 0, 0, 16, 89, 1, 0, 0, 0, 18, 107, 1, 0, 0, 0, 20, 109, 1, 0, 0, 0, 22, 111,
        1, 0, 0, 0, 24, 122, 1, 0, 0, 0, 26, 130, 1, 0, 0, 0, 28, 146, 1, 0, 0, 0, 30, 150, 1, 0,
        0, 0, 32, 157, 1, 0, 0, 0, 34, 172, 1, 0, 0, 0, 36, 187, 1, 0, 0, 0, 38, 189, 1, 0, 0, 0,
        40, 49, 3, 2, 1, 0, 41, 49, 3, 6, 3, 0, 42, 49, 3, 22, 11, 0, 43, 49, 3, 26, 13, 0, 44, 49,
        3, 30, 15, 0, 45, 49, 3, 32, 16, 0, 46, 49, 3, 38, 19, 0, 47, 49, 5, 0, 0, 1, 48, 40, 1,
        0, 0, 0, 48, 41, 1, 0, 0, 0, 48, 42, 1, 0, 0, 0, 48, 43, 1, 0, 0, 0, 48, 44, 1, 0, 0, 0, 48,
        45, 1, 0, 0, 0, 48, 46, 1, 0, 0, 0, 48, 47, 1, 0, 0, 0, 49, 1, 1, 0, 0, 0, 50, 51, 5, 1, 0,
        0, 51, 52, 3, 4, 2, 0, 52, 53, 5, 46, 0, 0, 53, 3, 1, 0, 0, 0, 54, 55, 5, 38, 0, 0, 55, 5,
        1, 0, 0, 0, 56, 57, 5, 2, 0, 0, 57, 58, 3, 8, 4, 0, 58, 59, 5, 3, 0, 0, 59, 61, 3, 12, 6, 0,
        60, 62, 3, 14, 7, 0, 61, 60, 1, 0, 0, 0, 61, 62, 1, 0, 0, 0, 62, 63, 1, 0, 0, 0, 63, 64, 5,
        46, 0, 0, 64, 7, 1, 0, 0, 0, 65, 70, 3, 10, 5, 0, 66, 67, 5, 4, 0, 0, 67, 69, 3, 10, 5, 0,
        68, 66, 1, 0, 0, 0, 69, 72, 1, 0, 0, 0, 70, 68, 1, 0, 0, 0, 70, 71, 1, 0, 0, 0, 71, 75, 1,
        0, 0, 0, 72, 70, 1, 0, 0, 0, 73, 75, 5, 5, 0, 0, 74, 65, 1, 0, 0, 0, 74, 73, 1, 0, 0, 0, 75,
        9, 1, 0, 0, 0, 76, 77, 5, 38, 0, 0, 77, 11, 1, 0, 0, 0, 78, 79, 5, 38, 0, 0, 79, 13, 1, 0,
        0, 0, 80, 81, 5, 6, 0, 0, 81, 86, 3, 16, 8, 0, 82, 83, 7, 0, 0, 0, 83, 85, 3, 16, 8, 0, 84,
        82, 1, 0, 0, 0, 85, 88, 1, 0, 0, 0, 86, 84, 1, 0, 0, 0, 86, 87, 1, 0, 0, 0, 87, 15, 1, 0, 0,
        0, 88, 86, 1, 0, 0, 0, 89, 90, 3, 10, 5, 0, 90, 91, 3, 18, 9, 0, 91, 92, 3, 20, 10, 0, 92,
        17, 1, 0, 0, 0, 93, 108, 5, 9, 0, 0, 94, 108, 5, 10, 0, 0, 95, 108, 5, 11, 0, 0, 96, 108,
        5, 12, 0, 0, 97, 108, 5, 13, 0, 0, 98, 108, 5, 14, 0, 0, 99, 101, 5, 15, 0, 0, 100, 99,
        1, 0, 0, 0, 100, 101, 1, 0, 0, 0, 101, 102, 1, 0, 0, 0, 102, 108, 5, 16, 0, 0, 103, 105,
        5, 15, 0, 0, 104, 103, 1, 0, 0, 0, 104, 105, 1, 0, 0, 0, 105, 106, 1, 0, 0, 0, 106, 108,
        5, 17, 0, 0, 107, 93, 1, 0, 0, 0, 107, 94, 1, 0, 0, 0, 107, 95, 1, 0, 0, 0, 107, 96, 1, 0,
        0, 0, 107, 97, 1, 0, 0, 0, 107, 98, 1, 0, 0, 0, 107, 100, 1, 0, 0, 0, 107, 104, 1, 0, 0,
        0, 108, 19, 1, 0, 0, 0, 109, 110, 7, 1, 0, 0, 110, 21, 1, 0, 0, 0, 111, 112, 5, 18, 0, 0,
        112, 113, 3, 12, 6, 0, 113, 114, 5, 19, 0, 0, 114, 115, 3, 8, 4, 0, 115, 116, 5, 20, 0,
        0, 116, 117, 5, 21, 0, 0, 117, 118, 5, 19, 0, 0, 118, 119, 3, 24, 12, 0, 119, 120, 5,
        20, 0, 0, 120, 121, 5, 46, 0, 0, 121, 23, 1, 0, 0, 0, 122, 127, 3, 20, 10, 0, 123, 124,
        5, 4, 0, 0, 124, 126, 3, 20, 10, 0, 125, 123, 1, 0, 0, 0, 126, 129, 1, 0, 0, 0, 127, 125,
        1, 0, 0, 0, 127, 128, 1, 0, 0, 0, 128, 25, 1, 0, 0, 0, 129, 127, 1, 0, 0, 0, 130, 131, 5,
        22, 0, 0, 131, 132, 3, 12, 6, 0, 132, 133, 5, 23, 0, 0, 133, 138, 3, 28, 14, 0, 134, 135,
        5, 4, 0, 0, 135, 137, 3, 28, 14, 0, 136, 134, 1, 0, 0, 0, 137, 140, 1, 0, 0, 0, 138, 136,
        1, 0, 0, 0, 138, 139, 1, 0, 0, 0, 139, 142, 1, 0, 0, 0, 140, 138, 1, 0, 0, 0, 141, 143,
        3, 14, 7, 0, 142, 141, 1, 0, 0, 0, 142, 143, 1, 0, 0, 0, 143, 144, 1, 0, 0, 0, 144, 145,
        5, 46, 0, 0, 145, 27, 1, 0, 0, 0, 146, 147, 3, 10, 5, 0, 147, 148, 5, 9, 0, 0, 148, 149,
        3, 20, 10, 0, 149, 29, 1, 0, 0, 0, 150, 151, 5, 24, 0, 0, 151, 153, 3, 12, 6, 0, 152, 154,
        3, 14, 7, 0, 153, 152, 1, 0, 0, 0, 153, 154, 1, 0, 0, 0, 154, 155, 1, 0, 0, 0, 155, 156,
        5, 46, 0, 0, 156, 31, 1, 0, 0, 0, 157, 158, 5, 25, 0, 0, 158, 159, 7, 2, 0, 0, 159, 160,
        3, 12, 6, 0, 160, 161, 5, 19, 0, 0, 161, 166, 3, 34, 17, 0, 162, 163, 5, 4, 0, 0, 163,
        165, 3, 34, 17, 0, 164, 162, 1, 0, 0, 0, 165, 168, 1, 0, 0, 0, 166, 164, 1, 0, 0, 0, 166,
        167, 1, 0, 0, 0, 167, 169, 1, 0, 0, 0, 168, 166, 1, 0, 0, 0, 169, 170, 5, 20, 0, 0, 170,
        171, 5, 46, 0, 0, 171, 33, 1, 0, 0, 0, 172, 173, 3, 10, 5, 0, 173, 174, 3, 36, 18, 0, 174,
        35, 1, 0, 0, 0, 175, 188, 5, 28, 0, 0, 176, 188, 5, 29, 0, 0, 177, 178, 5, 30, 0, 0, 178,
        179, 5, 19, 0, 0, 179, 180, 5, 39, 0, 0, 180, 188, 5, 20, 0, 0, 181, 188, 5, 31, 0, 0,
        182, 188, 5, 32, 0, 0, 183, 188, 5, 33, 0, 0, 184, 188, 5, 34, 0, 0, 185, 188, 5, 35,
        0, 0, 186, 188, 5, 36, 0, 0, 187, 175, 1, 0, 0, 0, 187, 176, 1, 0, 0, 0, 187, 177, 1, 0,
        0, 0, 187, 181, 1, 0, 0, 0, 187, 182, 1, 0, 0, 0, 187, 183, 1, 0, 0, 0, 187, 184, 1, 0,
        0, 0, 187, 185, 1, 0, 0, 0, 187, 186, 1, 0, 0, 0, 188, 37, 1, 0, 0, 0, 189, 190, 5, 37,
        0, 0, 190, 191, 7, 2, 0, 0, 191, 192, 5, 38, 0, 0, 192, 193, 5, 46, 0, 0, 193, 39, 1, 0,
        0, 0, 14, 48, 61, 70, 74, 86, 100, 104, 107, 127, 138, 142, 153, 166, 187
    ]


class customSQLParser(Parser):
    grammarFileName = "customSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'USE'", "'SELECT'", "'FROM'", "','",
                    "'*'", "'WHERE'", "'AND'", "'OR'", "'='", "'>'", "'<'",
                    "'>='", "'<='", "'!='", "'NOT'", "'LIKE'", "'IN'",
                    "'INSERT INTO'", "'('", "')'", "'VALUES'", "'UPDATE'",
                    "'SET'", "'DELETE FROM'", "'CREATE'", "'TABLE'", "'SCHEMA'",
                    "'UINT'", "'INT'", "'VARCHAR'", "'USHORT'", "'SHORT'",
                    "'ULONG'", "'LONG'", "'FLOAT'", "'DOUBLE'", "'DROP'",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "';'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "STRING",
                     "BOOLEAN", "WS", "COMMENT", "MULTI_COMMENT", "END"]

    RULE_statement = 0
    RULE_use_statement = 1
    RULE_schema_name = 2
    RULE_select_statement = 3
    RULE_columns = 4
    RULE_column = 5
    RULE_table_name = 6
    RULE_where_clause = 7
    RULE_condition = 8
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

    ruleNames = ["statement", "use_statement", "schema_name", "select_statement",
                 "columns", "column", "table_name", "where_clause", "condition",
                 "operator", "value", "insert_statement", "values", "update_statement",
                 "assignment", "delete_statement", "create_statement",
                 "column_def", "type", "drop_statement"]

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
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    ID = 38
    INT = 39
    FLOAT = 40
    STRING = 41
    BOOLEAN = 42
    WS = 43
    COMMENT = 44
    MULTI_COMMENT = 45
    END = 46

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

        def use_statement(self):
            return self.getTypedRuleContext(customSQLParser.Use_statementContext, 0)

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

        def EOF(self):
            return self.getToken(customSQLParser.EOF, 0)

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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.use_statement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.select_statement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.insert_statement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.update_statement()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.delete_statement()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.create_statement()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.drop_statement()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 47
                self.match(customSQLParser.EOF)
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

    class Use_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def schema_name(self):
            return self.getTypedRuleContext(customSQLParser.Schema_nameContext, 0)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_use_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUse_statement"):
                listener.enterUse_statement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUse_statement"):
                listener.exitUse_statement(self)

    def use_statement(self):

        localctx = customSQLParser.Use_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_use_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(customSQLParser.T__0)
            self.state = 51
            self.schema_name()
            self.state = 52
            self.match(customSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Schema_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(customSQLParser.ID, 0)

        def getRuleIndex(self):
            return customSQLParser.RULE_schema_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSchema_name"):
                listener.enterSchema_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSchema_name"):
                listener.exitSchema_name(self)

    def schema_name(self):

        localctx = customSQLParser.Schema_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_schema_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(customSQLParser.ID)
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

        def columns(self):
            return self.getTypedRuleContext(customSQLParser.ColumnsContext, 0)

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
        self.enterRule(localctx, 6, self.RULE_select_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(customSQLParser.T__1)
            self.state = 57
            self.columns()
            self.state = 58
            self.match(customSQLParser.T__2)
            self.state = 59
            self.table_name()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 6:
                self.state = 60
                self.where_clause()

            self.state = 63
            self.match(customSQLParser.END)
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
        self.enterRule(localctx, 8, self.RULE_columns)
        self._la = 0  # Token type
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.column()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 4:
                    self.state = 66
                    self.match(customSQLParser.T__3)
                    self.state = 67
                    self.column()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(customSQLParser.T__4)
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
        self.enterRule(localctx, 10, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
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
        self.enterRule(localctx, 12, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
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

        def condition(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(customSQLParser.ConditionContext, i)

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
        self.enterRule(localctx, 14, self.RULE_where_clause)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(customSQLParser.T__5)
            self.state = 81
            self.condition()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 7 or _la == 8:
                self.state = 82
                _la = self._input.LA(1)
                if not (_la == 7 or _la == 8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 83
                self.condition()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def column(self):
            return self.getTypedRuleContext(customSQLParser.ColumnContext, 0)

        def operator(self):
            return self.getTypedRuleContext(customSQLParser.OperatorContext, 0)

        def value(self):
            return self.getTypedRuleContext(customSQLParser.ValueContext, 0)

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
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.column()
            self.state = 90
            self.operator()
            self.state = 91
            self.value()
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(customSQLParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(customSQLParser.T__9)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(customSQLParser.T__10)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(customSQLParser.T__11)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.match(customSQLParser.T__12)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.match(customSQLParser.T__13)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 99
                    self.match(customSQLParser.T__14)

                self.state = 102
                self.match(customSQLParser.T__15)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 103
                    self.match(customSQLParser.T__14)

                self.state = 106
                self.match(customSQLParser.T__16)
                pass


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

        def FLOAT(self):
            return self.getToken(customSQLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(customSQLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(customSQLParser.BOOLEAN, 0)

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
            self.state = 109
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
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

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def columns(self):
            return self.getTypedRuleContext(customSQLParser.ColumnsContext, 0)

        def values(self):
            return self.getTypedRuleContext(customSQLParser.ValuesContext, 0)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
            self.state = 111
            self.match(customSQLParser.T__17)
            self.state = 112
            self.table_name()
            self.state = 113
            self.match(customSQLParser.T__18)
            self.state = 114
            self.columns()
            self.state = 115
            self.match(customSQLParser.T__19)
            self.state = 116
            self.match(customSQLParser.T__20)
            self.state = 117
            self.match(customSQLParser.T__18)
            self.state = 118
            self.values()
            self.state = 119
            self.match(customSQLParser.T__19)
            self.state = 120
            self.match(customSQLParser.END)
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
            self.state = 122
            self.value()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 123
                self.match(customSQLParser.T__3)
                self.state = 124
                self.value()
                self.state = 129
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

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def assignment(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(customSQLParser.AssignmentContext, i)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
            self.state = 130
            self.match(customSQLParser.T__21)
            self.state = 131
            self.table_name()
            self.state = 132
            self.match(customSQLParser.T__22)
            self.state = 133
            self.assignment()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 134
                self.match(customSQLParser.T__3)
                self.state = 135
                self.assignment()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 6:
                self.state = 141
                self.where_clause()

            self.state = 144
            self.match(customSQLParser.END)
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
            self.state = 146
            self.column()
            self.state = 147
            self.match(customSQLParser.T__8)
            self.state = 148
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

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
            self.state = 150
            self.match(customSQLParser.T__23)
            self.state = 151
            self.table_name()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 6:
                self.state = 152
                self.where_clause()

            self.state = 155
            self.match(customSQLParser.END)
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

        def table_name(self):
            return self.getTypedRuleContext(customSQLParser.Table_nameContext, 0)

        def column_def(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(customSQLParser.Column_defContext)
            else:
                return self.getTypedRuleContext(customSQLParser.Column_defContext, i)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
            self.state = 157
            self.match(customSQLParser.T__24)
            self.state = 158
            _la = self._input.LA(1)
            if not (_la == 26 or _la == 27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 159
            self.table_name()
            self.state = 160
            self.match(customSQLParser.T__18)
            self.state = 161
            self.column_def()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4:
                self.state = 162
                self.match(customSQLParser.T__3)
                self.state = 163
                self.column_def()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(customSQLParser.T__19)
            self.state = 170
            self.match(customSQLParser.END)
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
            self.state = 172
            self.column()
            self.state = 173
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
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(customSQLParser.T__27)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(customSQLParser.T__28)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(customSQLParser.T__29)
                self.state = 178
                self.match(customSQLParser.T__18)
                self.state = 179
                self.match(customSQLParser.INT)
                self.state = 180
                self.match(customSQLParser.T__19)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.match(customSQLParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(customSQLParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.match(customSQLParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.match(customSQLParser.T__33)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.match(customSQLParser.T__34)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 9)
                self.state = 186
                self.match(customSQLParser.T__35)
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

    class Drop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(customSQLParser.ID, 0)

        def END(self):
            return self.getToken(customSQLParser.END, 0)

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
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(customSQLParser.T__36)
            self.state = 190
            _la = self._input.LA(1)
            if not (_la == 26 or _la == 27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self.match(customSQLParser.ID)
            self.state = 192
            self.match(customSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
