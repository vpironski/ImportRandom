import os

import Engine.lib.tabulate as tabulate

import Engine.Main.db_engine_main as eng
import Engine.Main.generate_table as gen

os.chdir('./Engine/')
print('Do you want to enable colored output? (Might not work on some machines)')
print('Here is a sample to confirm if it works on yours: ')
print('underline: \033[4mThis text is underlined.\033[0m')
print('warn: \033[93mThis text is a warning.\033[0m')
print('critical: \033[91mThis text is a critical warning.\033[0m')
if input('Do you want to enable colors?: [y/n]') == 'y':
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'
    BOLD = OKBLUE
    UNDERLINE = OKGREEN
else:
    HEADER = ''
    OKBLUE = ''
    OKCYAN = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''


def divisor(): print('-' * 50 + '\n')


def warn(prompt: str): print(WARNING + prompt + ENDC)


def fail(prompt: str): print(FAIL + prompt + ENDC)


def get_column_values(column_names):
    values = []
    for col_name in column_names:
        value = input(f"{BOLD}Enter a value for {UNDERLINE}{col_name}: {ENDC}")
        values.append(value)
    return values


def input_choice(options_: tuple):
    options_ = list(options_)
    options_ = ['BACK'] + options_
    divisor()
    for i, item in enumerate(options_):
        print("{}. {}".format(i, item))
    print(f'When choosing you have to write the number that represents your choice above.')
    print(f"{BOLD}Please choose one of the above options: {ENDC}")
    while True:
        choice_ = input()
        if choice_.isnumeric() and 0 <= int(choice_) <= len(options_):
            break
        else:
            warn("Invalid choice. Please try again. ")
    return options_[int(choice_)]


def input_int(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            warn('Invalid value. Please try again. ')
    return number


def input_yes_no(prompt: str):
    answer = input(prompt + '[yes/no]')
    return answer.strip().lower() == 'yes'


def input_default(prompt: str, _int: bool = False):
    input_str = input(prompt).strip()
    if _int:
        while input_str.strip() != '':
            try:
                return int(input_str)
            except ValueError:
                input_str = input(f'{WARNING}Invalid value. Please try again. {ENDC}')

    if input_str == '':
        return None
    return input_str


def choose_table(db_name: str):
    return input_choice(tuple(os.listdir(f'./Databases/{db_name}')))


def table_structure_info(database: eng.Database, table_name_: str): return tabulate.tabulate(
    database.tables.get(table_name_).get_structure_info(),
    tablefmt=tabulate.tabulate_formats[3],
    headers=('column', 'type', 'length'))


def table_sizes(dbase: eng.Database):
    data = []
    for table in dbase.tables.values():
        data.append((table.name, table.current_entry_count))
    if data:
        return tabulate.tabulate(data,
                                 tablefmt=tabulate.tabulate_formats[3],
                                 headers=('name', 'rows'))
    else:
        return None
    pass


stopped = False
while True:
    is_open = False
    while not is_open:
        db = None
        options = ('USE', 'DROP', 'CREATE', 'GENERATE')
        databases = tuple(os.listdir('./Databases/'))
        choice = input_choice(options)
        if choice == options[0]:
            db = input_choice(databases)
            if db == 'BACK':
                continue
            db = eng.Database(db)
            print(table_sizes(db))
            is_open = True

        elif choice == options[1]:
            db = input_choice(databases)
            if db == 'BACK':
                continue
            db = eng.Database(db)
            if input_yes_no(f'{WARNING}Are you sure you want to permanently delete {db.name}'):
                db.drop_schema()
                print(f'{OKGREEN}Success.{ENDC}')

        elif choice == options[2]:
            name = input(f'Enter name of schema {BOLD}(or 0 to return to menu){ENDC}: ')
            if name == '0':
                continue
            try:
                eng.Database.create(name)
            except eng.CreationError as e:
                fail(e.message)

        elif choice == options[3]:
            print(
                f'The generate method creates a new schema/database {OKGREEN}generated{ENDC} and inside, a new table {OKGREEN}worker{ENDC}.',
                '\nTable info: ')
            print(table_structure_info(eng.Database('generated'), 'worker'))
            print(f'\n{BOLD}Enter 0 to return to menu.{ENDC}')
            count = input_int(f'How many rows would you like to generate? {OKCYAN}(int){ENDC}:')
            if count == 0:
                continue
            gen.generate(count)

        elif choice == 'BACK':
            stopped = True
            break
    if stopped:
        break

    while True:
        # db was opened ->
        options = ('SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COUNT ROWS', 'CREATE TABLE', 'DROP TABLE')
        choice = input_choice(options)
        # select
        if choice == options[0]:
            choice = choose_table(db.name)
            if choice == 'BACK':
                continue
            print(f'Table info for {BOLD}{choice}{ENDC}: ')
            print(table_structure_info(db, choice))
            print('Please provide the options needed for select...')
            print(f'{UNDERLINE}You can leave each of the following options empty for defaults.{ENDC}')
            columns = input_default(f'Input the columns you want to display {OKCYAN}(comma separated){ENDC}: ')
            if columns is not None:
                columns = list(columns.replace(' ', '').split(','))
            start = input_default(f'Enter the index at which you want to start searching {OKCYAN}(int){ENDC}: ',
                                  _int=True)
            limit = input_default(f'Enter a limit {OKCYAN}(int){ENDC}: ', _int=True)
            print(
                f'The condition should be in the following format: {OKCYAN}<column_name> <operator> <value> and/or ... {ENDC}')
            print(f'Possible operators are: {OKCYAN}=, !=, >, >=, <, <=, in, not in, like{ENDC}')
            print(f'{OKCYAN}"in"{ENDC} and {OKCYAN}"not in"{ENDC} take a tuple like syntax: (1, 2, 3)')
            print(f'{OKCYAN}"like"{ENDC} takes any valid regex')
            condition = input_default('Enter the condition (or leave blank): ')
            try:
                result = db.linear_select(choice, columns, start, limit, condition)
                print(tabulate.tabulate(result, tablefmt=tabulate.tabulate_formats[3],
                                        headers=[a[0] for a in db.tables.get(choice).translator.config]))
            except eng.InvalidTableError as e:
                fail(e.message)
            except eng.InvalidSyntaxError as e:
                fail(e.message)
            pass
        # insert
        elif choice == options[1]:
            choice = choose_table(db.name)
            if choice == 'BACK':
                continue
            print(f'Table info for {BOLD}{choice}{ENDC}: ')
            print(table_structure_info(db, choice))
            print('Please provide the column values needed for insert...')
            try:
                db.insert(choice, get_column_values(db.tables.get(choice).get_functional_column_names()))
            except eng.InvalidTableError as e:
                fail(e.message)
            except eng.InvalidIDError as e:
                fail("Invalid id!")
            except eng.InvalidSyntaxError as e:
                fail(e.message)
            pass
        # update/delete
        elif choice in options[2:3:]:
            table_name = choose_table(db.name)
            if choice == 'BACK':
                continue
            print(f'Table info for {BOLD}{table_name}{ENDC}: ')
            print(table_structure_info(db, table_name))
            while True:
                id_index = input_int('Select an ID: ')
                try:
                    result = [db.tables.get(table_name).read(id_index)]
                except eng.InvalidIDError as e:
                    fail('Invalid id!')
                except eng.InvalidSyntaxError as e:
                    fail(e.message)
                print(tabulate.tabulate(result, tablefmt=tabulate.tabulate_formats[3],
                                        headers=[a[0] for a in db.tables.get(table_name).translator.config]))
                if input_yes_no('Are you satisfied with the choice of entry?'):
                    break

            # update
            if choice == options[2]:
                result = db.tables.get(table_name).get_labeled_entry(result[0])
                del result['id']
                del result['inf']
                print(f'Please input the changes to the entry {UNDERLINE}(leave empty for default){ENDC}: ')
                changes = dict()
                for column in result:
                    change = input(f'Enter new value for {BOLD}{column}{ENDC}: ')
                    if change == '':
                        continue
                    changes[column] = change
                try:
                    db.update(choice, id_index, changes)
                except eng.InvalidTableError as e:
                    fail(e.message)

            # delete
            elif choice == options[3]:
                db.delete(table_name, id_index)
            pass
        # count
        elif choice == options[4]:
            print(table_structure_info(db, choice))
            pass

        # create table
        elif choice == options[5]:
            # structure -> list( tuple(<name>, <type>, <length>)) where each inner tuple represents a new column
            print('Create table....')
            print('You will be prompted to enter all data needed for creating a new table.')
            table_name = input('Choose a table name: ')
            if not input_yes_no(
                    f'You are about to create {BOLD}{db.name}.{table_name}{BOLD} . {UNDERLINE}Do you wish to continue?{ENDC} '):
                continue
            print('Names must start with any letter and can include upper and lower case letters, numbers and _')
            print('Available datatypes: ')
            print(tabulate.tabulate([[a, eng.data_types_descriptive.get(a)] for a in eng.data_types_descriptive],
                                    tablefmt=tabulate.tabulate_formats[3]))
            columns = []
            while True:
                column_name = input(f"Enter column name {UNDERLINE}(or 'done' to finish){ENDC}: ")
                if column_name.lower().strip() == "done":
                    break
                column_type = input("Enter column type: ")
                column_length = input_int("Enter column length: ")
                columns.append((column_name, column_type, column_length))
            try:
                db.create_table(table_name, columns)
            except eng.CreationError as e:
                fail(e.message)
            pass

        # drop table
        elif choice == options[6]:
            table_name = choose_table(db.name)
            if choice == 'BACK':
                continue
            if input_yes_no(f'{WARNING}Are you sure you want to permanently delete {table_name}? {ENDC}'):
                db.tables.get(table_name).drop()
            pass
        elif choice == 'BACK':
            del db
            break
            pass
