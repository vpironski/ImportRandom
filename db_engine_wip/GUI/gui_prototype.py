from tkinter import *
from tkinter import filedialog
from tkinter_additional_classes import *
from db_engine import database_core
from db_engine import database_utils
from db_engine import database_select
from db_engine.database_core import Database

hints = [
    'Column names: 1 word only [a-z](uppercase too) \n or multiple words divided with \'_\'. ',
    f'Available types: {database_core.types_length.keys()}',
    'Column types or length: number (length) or type (see available types).',
    '-- \'date\' - YYYY-MM-DD (2001-03-27)',
    '-- \'gender\' - m/f/n',
    '-- \'course_number\' - exactly 5 digits long (19201)',
    'Important: Select function works with regexes too for broader searches.'
]


def open_db():
    clear(error_frame)
    clear(main_frame)
    global is_open
    global db
    if not is_open:
        filename = filedialog.askopenfilename(initialdir='../Databases/',
                                              title='Select a database',
                                              filetypes=(('databases', database_core.database_extension),))
        if filename:
            db = Database(filename)
            is_open = True
            global open_label_text
            open_label_text = f'Currently open: {db.name}.'
            update_open_label()
    else:
        error_handler(['You already have a database open!'])


def close():
    clear(main_frame)
    clear(error_frame)
    global is_open
    global db
    global open_label_text
    if is_open:
        db.close()
        is_open = False
        open_label_text = 'No database is currently open.'
        update_open_label()
    else:
        error_handler(['No database is open!'])


def drop():
    close()
    if is_open:
        db.drop()


def create():
    clear(main_frame)
    clear(error_frame)
    if is_open:
        error_handler(['Please close the database before creating a new one!'])
        return

    # doesn't have a check for columns with the same names!
    input_frame_row = 0
    input_frame_column = 0

    def delete():
        nonlocal input_frame_row
        nonlocal input_frame_column
        if create_input_frame.grid_slaves():
            create_input_frame.grid_slaves()[0].grid_forget()
            input_frame_row -= 1

            if input_frame_row < 0:
                input_frame_row = 5
                input_frame_column -= 1
        else:
            error_handler(['Nothing to delete!'])

    def add():
        nonlocal input_frame_row
        nonlocal input_frame_column
        clear(error_frame)
        text = ''
        name_text = name.get()
        length_text = length.get()

        if not name_text == '' and not length_text == '':
            if Database.validate_name(name_text):
                text += name_text + ','
                if length_text.isnumeric():
                    text += length_text
                else:
                    if length_text in database_core.types_length:
                        text += f'|{length_text}|'
                    else:
                        error_handler(['Type not found!'])
                        return
                if input_frame_row == 5:
                    input_frame_row = 0
                    input_frame_column += 1

                Label(create_input_frame, text=text).grid(row=input_frame_row, column=input_frame_column, sticky='W')
                name.delete(0, END)
                length.delete(0, END)
                input_frame_row += 1
            else:
                error_handler(['Incorrect column name value! See hints.'])
        else:
            error_handler(['Please fill in both boxes.'])
        pass

    def create_db():
        conf_dict = dict()
        has_duplicates = False
        if create_input_frame.grid_slaves():
            if db_name.get():
                input_labels = list[Label](create_input_frame.grid_slaves())
                input_labels.reverse()
                for column in input_labels:
                    raw_name = column['text'].split(',')
                    col_name = raw_name[0]
                    col_type = raw_name[1]
                    if col_name not in conf_dict.keys():
                        conf_dict.update({col_name: col_type})
                    else:
                        has_duplicates = True
                        break
                if not has_duplicates:
                    Database.create(conf_dict, db_name.get())
                    clear(main_frame)
                else:
                    error_handler(['There must not be duplicate names of columns!'])
            else:
                error_handler(['Please specify a database name.'])
        else:
            error_handler(['Cannot create database with 0 columns'])

    Label(main_frame, text='Name of the database').grid(row=0, column=0)
    db_name = Entry(main_frame)
    db_name.grid(row=1, column=0, padx=3, pady=1)

    Label(main_frame, text='Name of column:').grid(row=2, column=0)
    name = Entry(main_frame)
    name.grid(row=3, column=0, padx=3, pady=1)

    Label(main_frame, text='Size or type:').grid(row=2, column=1)
    length = Entry(main_frame)
    length.grid(row=3, column=1, padx=3, pady=1)

    Button(main_frame, text='Add', command=add).grid(row=3, column=2, ipadx=20)
    Button(main_frame, text='Create', command=create_db).grid(row=1, column=1, sticky='W', padx=10)
    Label(main_frame, text='Press after adding all the columns.').grid(row=0, column=1, columnspan=2, sticky='W')
    create_input_frame = Frame(main_frame, width=400, height=40, relief=SUNKEN, bd=3)
    create_input_frame.grid(row=4, columnspan=4, sticky='NW', ipadx=10, ipady=5)

    Button(main_frame, text='Delete', command=delete).grid(row=5)
    # add hints for available types
    pass


def insert():
    clear(error_frame)
    clear(main_frame)

    def add_to_db():
        clear(error_frame)
        values_list = ['1']  # is_active
        values_list += insert_input_frame.read_input().values()
        errors = database_utils.insert(db, values_list)
        if errors is not None:
            error_handler(errors)
        else:
            for val in list[Entry](insert_input_frame.grid_slaves(column=1) + insert_input_frame.grid_slaves(
                    column=4) + insert_input_frame.grid_slaves(column=7)):
                val.delete(0, END)
        # clear widgets

    if is_open:
        insert_input_frame = TableInputFrame(main_frame, db.colons_types)
        insert_input_frame.grid()

        Button(main_frame, text='Insert', width=10, bg='green', fg='white', command=add_to_db) \
            .grid(padx=3, pady=3, ipadx=3, ipady=3)
    else:
        error_handler(['You have to have a database open to insert into.'])


def select():
    def show_results():
        clear(main_frame)
        nonlocal select_input_frame
        filters = select_input_frame.read_input()
        filters = filters if filters != {} else None
        row_ids = database_select.select(db, filters)

        dictionary = db.colons_types.copy()
        del dictionary['is_active']
        for column, length in zip(dictionary.keys(), dictionary.values()):
            if type(length) is not int:
                dictionary.update({column: database_core.types_length[length]})
        dictionary.update({'Select': 1})

        table = SelectTable(main_frame, dictionary,
                            width=main_frame.winfo_width() - 60, height=600)
        table.grid(row=0, column=0, sticky='nsew', pady=10, padx=(20, 40))
        table.grid_propagate(False)

        Button(main_frame, text='DELETE SELECTED', command=lambda: delete(table)) \
            .grid(row=1, column=0, sticky='nw', padx=5, pady=5)
        Button(main_frame, text='UPDATE SELECTED', command=lambda: print('Not done yet!')) \
            .grid(row=1, column=1, sticky='nw', padx=5, pady=5)

        for row_id in row_ids:
            columns = list(database_select.get_dict(db, database_select.read_entry(db, row_id)).values())
            columns.pop(1)
            table.add_row(columns)

    def delete(table: SelectTable):
        selected = table.read_selected()
        for id_index in selected:
            print(id_index)
            database_utils.delete(db, id_index)

    clear(main_frame)
    if is_open:
        Label(main_frame, text='Write your search criteria here: ', font=("Segoe UI", 12, 'bold'))\
            .grid(padx=10, pady=10, sticky='nw')
        select_input_frame = TableInputFrame(main_frame, db.colons_types)
        select_input_frame.grid(padx=20, pady=20)
        Button(main_frame, text='Search', width=10, bg='green', fg='white', command=show_results) \
            .grid(padx=3, pady=3, ipadx=3, ipady=3)

    else:
        error_handler(['Please open a database to select from!'])


def error_handler(errors: list):
    clear(error_frame)
    Label(error_frame, text='Errors: ', font=("Segoe UI", 12, 'bold'), bg='#abaaa9')\
        .grid(row=0, sticky='nw', padx=3, pady=3)
    for error, row in zip(errors, range(len(errors))):
        Label(error_frame, text=error, bg='#abaaa9', font=("Segoe UI", 10, 'bold'))\
            .grid(row=row + 1, sticky='NW', padx=3, pady=3)


def clear(master):
    for widget in master.grid_slaves():
        widget.grid_forget()


def update_open_label():
    global open_label
    global open_label_text
    open_label.config(text=open_label_text)


root = Tk()
root.title('Import Random DB v1')
# root.iconbitmap("c:/vs.code/images/dice.ICO")
root.geometry('1760x990')
root.grid_columnconfigure(0, weight=5)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=2)

global db
is_open = False
open_label_text = 'No database currently open.'

navbar_frame = Frame(root, relief=RAISED, bd=3)
navbar_frame.grid(row=0, column=0, sticky='new', columnspan=2)
open_label = Label(navbar_frame, text=open_label_text)
open_label.grid(row=1, column=0, ipadx=3, ipady=3,
                padx=5, pady=5,
                columnspan=3)

navbar_buttons = [
    Button(navbar_frame, text="open", command=open_db),
    Button(navbar_frame, text="close", command=close),
    Button(navbar_frame, text="drop", command=drop),
    Button(navbar_frame, text="create", command=create),
    Button(navbar_frame, text="insert", command=insert),
    Button(navbar_frame, text="select", command=select),
    Button(navbar_frame, text="Exit", command=root.destroy)
]
for button, col in zip(navbar_buttons, range(len(navbar_buttons))):
    button.grid(row=0, column=col, ipadx=3, ipady=3, padx=5, pady=5)

main_frame = Frame(root)
main_frame.grid(row=1, column=0, sticky='nsew', rowspan=2)
main_frame.grid_propagate(False)

error_frame = Frame(root, relief=SUNKEN, bd=3, bg='#abaaa9')
error_frame.grid(row=1, column=1, sticky='nsew')
error_frame.grid_propagate(False)

hint_frame = Frame(root, relief=SUNKEN, bd=3, bg='#abaaa9')
hint_frame.grid(row=2, column=1, sticky='nsew')
hint_frame.grid_propagate(False)
Label(hint_frame, text='Hints:', font=("Segoe UI", 12, 'bold'), bg='#abaaa9').grid(sticky='new')
for hint in hints:
    Label(hint_frame, text=hint, bg='#abaaa9', font=("Segoe UI", 10, 'bold')).grid(sticky='nw', pady=5, padx=5)

root.mainloop()
