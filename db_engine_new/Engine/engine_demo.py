import os
import sys

import db_engine_new.Engine.Main.db_engine_main as eng
import db_engine_new.Engine.Tests.generate_table as gen
import tabulate
import argparse


def get_column_values(column_names):
    values = []
    for col_name in column_names:
        value = input(f"Enter a value for {col_name}: ")
        values.append(value)
    return values


def input_choice(options_: tuple):
    print('--------------------------------------------------------------------------')
    for i, item in enumerate(options_):
        print("{}. {}".format(i + 1, item))
    print("Please choose one of the above options:")
    while True:
        choice_ = input()
        if choice_.isnumeric() and 1 <= int(choice_) <= len(options_):
            break
        else:
            print("Invalid choice. Please try again.")
    return options[int(choice_) - 1]


def input_int(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print('Invalid value.')
    return number


def input_yes_no(prompt: str):
    answer = input(prompt + '[yes/no]')
    return answer.strip().lower() == 'yes'


def choose_table(db_name: str): return input_choice(tuple(os.listdir(f'./Databases/{db_name}')))


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
        options = ('USE', 'DROP', 'CREATE', 'GENERATE', 'EXIT DEMO')
        databases = tuple(os.listdir('./Databases/'))
        choice = input_choice(options)
        if choice == options[0]:
            db = eng.Database(input_choice(databases))
            print(table_sizes(db))
            is_open = True

        elif choice == options[1]:
            db = eng.Database(input_choice(databases))
            if input_yes_no(f'Are you sure you want to permanently delete {db.name}'):
                db.drop_schema()

        elif choice == options[2]:
            name = input('Enter name of schema')
            eng.Database.create(name)

        elif choice == options[3]:
            print('The generate method creates a new schema (generated) and inside, a new table (worker).',
                  'The table has columns: first_name, last_name, position, salary, identification')
            count = input_int('How many rows would you like to generate')
            gen.generate(count)

        else:
            stopped = True
            break
    if stopped:
        break

    while True:
        # db was opened ->
        options = ('SELECT', 'INSERT', 'UPDATE', 'DELETE', 'COUNT ROWS', 'CREATE TABLE', 'DROP TABLE', 'BACK')
        choice = input_choice(options)
        # select
        if choice == options[0]:
            choice = choose_table(db.name)
            print('--------------------------------------------------------------------------')
            print(f'Table info for {choice}: ')
            print(table_structure_info(db, choice))
            print('Please provide the options needed for select...')
            print('Possibilities are: --columns, --start, --limit, --condition')
            print('All arguments should be written exactly as above and space separated or left out for defaults.')
            print('--columns default is all')
            print('--start default is 0')
            print('--limit default is None')
            print('--condition default is None (example condition: column1 > 2 and column2 like \'A.*\'')
            print('possible conditional operators are: =, >, <, >=, <=, !=, in, not in, like')
            print('press CTRL + D after you are done. \n>>')
            parser = argparse.ArgumentParser()
            parser.add_argument("--columns", help="Enter columns (comma separated)", default=None)
            parser.add_argument("--start", help="Enter start", type=int, default=0)
            parser.add_argument("--limit", help="Enter limit", type=int, default=-1)
            parser.add_argument("--condition", help="Enter condition", default=None)
            args = parser.parse_args(sys.stdin.read().split())
            columns = args.columns.split(',') if args.columns else None
            result = db.linear_select(choice, columns, args.start, args.limit, args.condition)
            print(tabulate.tabulate(result, tablefmt=tabulate.tabulate_formats[3],
                                    headers=[a[0] for a in db.tables.get(choice).translator.config]))
            pass
        # insert
        elif choice == options[1]:
            choice = choose_table(db.name)
            print('--------------------------------------------------------------------------')
            print(f'Table info for {choice}: ')
            print(table_structure_info(db, choice))
            print('Please provide the column values needed for insert...')
            db.insert(choice, get_column_values(db.tables.get(choice).get_functional_column_names()))
            pass
        # update/delete
        elif choice in options[2:3:]:
            table_name = choose_table(db.name)
            print('--------------------------------------------------------------------------')
            print(f'Table info for {table_name}: ')
            print(table_structure_info(db, table_name))
            while True:
                id_index = input_int('Select an ID: ')
                result = [db.tables.get(table_name).read(id_index)]
                print(tabulate.tabulate(result, tablefmt=tabulate.tabulate_formats[3],
                                        headers=[a[0] for a in db.tables.get(table_name).translator.config]))
                if input_yes_no('Are you satisfied with the choice of entry?'):
                    break

            # update
            if choice == options[2]:
                result = db.tables.get(table_name).get_labeled_entry(result[0])
                del result['id']
                del result['inf']
                print('Please input the changes to the entry (leave empty for default): ')
                changes = dict()
                for column in result:
                    change = input(f'Enter new value for {column}: ')
                    if change == '':
                        continue
                    changes[column] = change
                db.update(choice, id_index, changes)

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
            if not input_yes_no(f'You are about to create {db.name}.{table_name} . Do you wish to continue? '):
                continue
            print('Names must start with any letter and can include upper and lower case letters, numbers and _')
            print('Available datatypes: ')
            print(tabulate.tabulate([[a, eng.data_types_descriptive.get(a)] for a in eng.data_types_descriptive],
                                    tablefmt=tabulate.tabulate_formats[3]))
            columns = []
            while True:
                column_name = input("Enter column name (or 'done' to finish): ")
                if column_name.lower() == "done":
                    break
                column_type = input("Enter column type: ")
                column_length = input_int("Enter column length: ")
                columns.append((column_name, column_type, column_length))
            db.create_table(table_name, columns)
            pass

        # drop table
        elif choice == options[6]:
            table_name = choose_table(db.name)
            if input_yes_no(f'Are you sure you want to permanently delete {table_name}'):
                db.tables.get(table_name).drop()
            pass
        else:
            del db
            break
            pass
