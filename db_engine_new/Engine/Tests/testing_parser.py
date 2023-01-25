import antlr4
from db_engine_new.Engine.Parser.customSQLLexer import customSQLLexer
from db_engine_new.Engine.Parser.customSQLParser import customSQLParser
from db_engine_new.Engine.Parser.customSQLListener import customSQLListener

# public static void main(String[] args)
# {
#         CharStream inputStream = CharStreams.fromString("sessionToken=abc123; Expires=Wed, 09 Jun 2021 10:18:14 GMT");
#         CookieLexer cookieLexer = new CookieLexer(inputStream);
#         CommonTokenStream commonTokenStream = new CommonTokenStream(cookieLexer);
#         CookieParser cookieParser = new CookieParser(commonTokenStream);
#
#         CookieContext cookieContext = cookieParser.cookie();
#         TalkingListener listener = new TalkingListener();
#         ParseTreeWalker.DEFAULT.walk(listener, cookieContext);
# }

query = 'SELECT column1, column2 FROM table_name WHERE column1 = "value" AND column2 NOT LIKE "sdkjhf";'
lexer = customSQLLexer(antlr4.InputStream(query))
token_stream = antlr4.CommonTokenStream(lexer)
parser = customSQLParser(token_stream)

context = parser.statement()
listener = customSQLListener()
antlr4.ParseTreeWalker.DEFAULT.walk(listener, context)



