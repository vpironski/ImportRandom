import os
from tkinter import *
from tkinter import filedialog

import database_core
from database_core import Database
import database_insert


# hints_for_types = {'date': ''}


def open_db():
    clear(main_frame)
    global is_open
    global db
    filename = filedialog.askopenfilename(initialdir=os.getcwd() + '/Databases',
                                          title='Select a database',
                                          filetypes=(('databases', database_core.file_extension),))
    if filename:
        db = Database(filename)
        is_open = True
        global open_label_text
        open_label_text = f'Currently open: {db.name}.'
        update_open_label()


def close():
    clear(main_frame)
    clear(error_frame)
    global is_open
    global db
    global open_label_text
    if is_open:
        db = None
        is_open = False
        open_label_text = 'No database is currently open.'
        update_open_label()
    else:
        # open_label.config(fg='red')
        pass


def drop():
    if is_open:
        db.drop()
        close()
    else:
        open_label.config(fg='red')


def create():
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
        if create_input_frame.grid_slaves():
            if db_name.get():
                for column in list[Label](create_input_frame.grid_slaves()):
                    raw_name = column['text'].split(',')
                    col_name = raw_name[0]
                    col_type = raw_name[1]
                    conf_dict.update({col_name: col_type})
                Database.create(conf_dict, db_name.get())
            else:
                error_handler(['Please specify a database name.'])
        else:
            error_handler(['Cannot create database with 0 columns'])

    close()
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
    def add_to_db():
        values_list = []
        for val in list[Entry](insert_input_frame.grid_slaves(column=1) + insert_input_frame.grid_slaves(
                column=4) + insert_input_frame.grid_slaves(column=7)):
            if not val.get() == '':
                values_list.append(val.get())
        values_list.reverse()
        errors = database_insert.insert(db, values_list)
        if errors is not None:
            error_handler(errors)
        else:
            clear(error_frame)
            for val in list[Entry](insert_input_frame.grid_slaves(column=1) + insert_input_frame.grid_slaves(
                    column=4) + insert_input_frame.grid_slaves(column=7)):
                val.delete(0, END)
        # clear widgets

    clear(main_frame)

    if is_open:
        insert_input_frame = Frame(main_frame)
        insert_input_frame.grid()
        grid_column = 0
        grid_row = 0
        for colon in db.colons.keys():
            Label(insert_input_frame, text=colon).grid(row=grid_row, column=grid_column, padx=3, pady=3, ipadx=3,
                                                       ipady=3)
            Entry(insert_input_frame).grid(row=grid_row, column=grid_column + 1, ipadx=3, ipady=3)
            Label(insert_input_frame, text=db.colons.get(colon)).grid(row=grid_row, column=grid_column + 2, padx=3,
                                                                      pady=3,
                                                                      ipadx=3, ipady=3)
            grid_row += 1
            if grid_row == 16:
                grid_row = 0
                grid_column += 3

        Button(main_frame, text='Insert', width=10, bg='green', fg='white', command=add_to_db).grid(padx=3,
                                                                                                    pady=3, ipadx=3,
                                                                                                    ipady=3)
    else:
        open_label.config(fg='red')


def error_handler(errors: list):
    clear(error_frame)
    for error, row in zip(errors, range(len(errors))):
        Label(error_frame, text=error, bg='gray', font=("Segoe UI", 10, 'normal')).grid(row=row, sticky='NW', padx=3,
                                                                                        pady=3)


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
root.geometry('1200x800')
root.grid_columnconfigure(0, weight=3, minsize=800)
root.grid_columnconfigure(1, weight=1, minsize=400)
root.grid_rowconfigure(1, weight=1)

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
    Button(navbar_frame, text="select"),
    Button(navbar_frame, text="Exit", command=root.destroy)
]
for button, col in zip(navbar_buttons, range(len(navbar_buttons))):
    button.grid(row=0, column=col, ipadx=3, ipady=3, padx=5, pady=5)

main_frame = Frame(root)
main_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')
main_frame.grid_propagate(False)

error_frame = Frame(root, relief=SUNKEN, bd=4, bg='#abaaa9')
error_frame.grid(row=1, column=1, columnspan=1, sticky='nsew')
error_frame.grid_propagate(False)

root.mainloop()
