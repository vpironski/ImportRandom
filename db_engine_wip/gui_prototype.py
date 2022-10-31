import os
from tkinter import *
from tkinter import filedialog

import database_core
from database_core import Database
import database_insert


# hints_for_types = {'date': ''}


def open_db():
    clear(root)
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
    clear(root)
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
        open_label.config(fg='red')


def drop():
    if is_open:
        db.drop()
        close()
    else:
        open_label.config(fg='red')


def create():
    close()
    
    # add hints for available types
    pass


def insert():
    def add_to_db():
        values_list = []
        for val in list[Entry](insert_input_frame.grid_slaves(column=1) + insert_input_frame.grid_slaves(
                column=3) + insert_input_frame.grid_slaves(column=6)):
            if not val.get() == '':
                values_list.append(val.get())
        values_list.reverse()
        error_handler(database_insert.insert(db, values_list))
        # clear widgets

    clear(root)

    if is_open:
        insert_master = Frame(root)
        insert_input_frame = Frame(insert_master)
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

        Button(insert_master, text='Insert', width=10, bg='green', fg='white', command=add_to_db).grid(padx=3,
                                                                                                       pady=3, ipadx=3,
                                                                                                       ipady=3)
        insert_master.grid(row=1, sticky='NW')
    else:
        open_label.config(fg='red')


def error_handler(errors: list):
    clear(error_frame)
    for error, row in zip(errors, range(len(errors))):
        Label(error_frame, text=error, bg='gray', font=("Segoe UI", 14, 'bold')).grid(row=row, sticky='NW', padx=3,
                                                                                      pady=3)


def clear(master):
    for widget in master.grid_slaves(row=1, column=0):
        widget.grid_forget()


def update_open_label():
    global open_label
    global open_label_text
    open_label.config(text=open_label_text, fg='black')


root = Tk()
root.title('Import Random DB v1')
# root.iconbitmap("c:/vs.code/images/dice.ICO")
root.geometry('1200x800')
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)

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

error_frame = Frame(root, relief=SUNKEN, bd=4, bg='gray', width=400, height=800)
error_frame.grid(row=1, column=1, sticky='NE')
error_frame.grid_propagate(False)

root.mainloop()
