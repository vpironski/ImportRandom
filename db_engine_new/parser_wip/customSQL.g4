grammar customSQL;

/* Statements */
statement : select_statement
          | insert_statement
          | update_statement
          | delete_statement
          | create_statement
          | drop_statement;

/* SELECT Statement */
select_statement : SELECT columns FROM table_name where_clause?;
columns : column (',' column)*;
column : ID;
table_name : ID;
where_clause : WHERE condition;
condition : comparison_expression;
comparison_expression : column comparison operator value;
comparison : EQ | NE | GT | LT | GE | LE;
operator : '=' | '>' | '<' | '>=' | '<=' | '<>';
value : INT | STRING;

/* INSERT Statement */
insert_statement : INSERT INTO table_name '(' columns ')' VALUES '(' values ')';
values : value (',' value)*;

/* UPDATE Statement */
update_statement : UPDATE table_name SET assignment (',' assignment)* where_clause?;
assignment : column '=' value;

/* DELETE Statement */
delete_statement : DELETE FROM table_name where_clause?;

/* CREATE Statement */
create_statement : CREATE TABLE table_name '(' column_def (',' column_def)* ')' ;
column_def : column type;
type : INT | VARCHAR;

/* DROP Statement */
drop_statement : DROP TABLE table_name;

/* Tokens */
ID : [a-zA-Z]+;
INT : [0-9]+;
STRING : '"' .*? '"';
WS : [ \t\r\n]+ -> skip;