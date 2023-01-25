grammar customSQL;

/* Statements */
statement : use_statement
	    | select_statement
          | insert_statement
          | update_statement
          | delete_statement
          | create_statement
          | drop_statement
	    | EOF;

/* USE Statement */
use_statement : 'USE' schema_name END;
schema_name : ID;

/* SELECT Statement */
select_statement : 'SELECT' columns 'FROM' table_name where_clause? END;
columns : (column (',' column)*) | '*';
column : ID;
table_name : ID;
where_clause : 'WHERE' condition (('AND'|'OR') condition)*;
condition : column operator value;
operator : '=' | '>' | '<' | '>=' | '<=' | '!=' | 'NOT'? 'LIKE' | 'NOT'? 'IN';
value : INT | FLOAT | STRING | BOOLEAN ;

/* INSERT Statement */
insert_statement : 'INSERT INTO' table_name '(' columns ')' 'VALUES' '(' values ')' END;
values : value (',' value)*;

/* UPDATE Statement */
update_statement : 'UPDATE' table_name 'SET' assignment (',' assignment)* where_clause? END;
assignment : column '=' value;

/* DELETE Statement */
delete_statement : 'DELETE FROM' table_name where_clause? END;

/* CREATE Statement */
create_statement : 'CREATE' ('TABLE' | 'SCHEMA') table_name '(' column_def (',' column_def)* ')' END;
column_def : column type;
type : 'UINT' | 'INT' | 'VARCHAR' '(' INT ')' | 'USHORT' | 'SHORT' | 'ULONG' | 'LONG' | 'FLOAT' | 'DOUBLE';

/* DROP Statement */
drop_statement : 'DROP' ('TABLE' | 'SCHEMA') ID END;

ID : [a-zA-Z][a-zA-Z0-9_]*;
INT : [0-9]+;
FLOAT : [0-9]+('.'[0-9]+)*;
STRING : '"' .*? '"';
BOOLEAN : 'True' | 'False';
WS : [ \t\r\n]+ -> skip;
COMMENT : '//'~[\r\n]* -> skip;
MULTI_COMMENT : '/*'.*?'*/' -> skip;
END : ';';