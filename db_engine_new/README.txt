This is a demo of ImportRandom's database engine. It's a simple cli application that demonstrates the functionality of the database engine.

Requirements:
	-python 3.10
	-tabulate --> included in demo
	-os 
	-re
	-shutil
	-pickle
	-struct
	-random 
	-string 
	-argparse

The demo also includes a test database (generated), which you can also generate yourselves (option for this is in the menu).
The engine currently has the following basic functionalities:
	-insert
	-update
	-delete
	-select
	-create (tables and databases/schemas)
The raw data of tables is saved in binary form. Serialization is done with pickle (for configs) and struct (for the data)
To try out the program run engine_demo.py