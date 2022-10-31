import os
from tkinter import *
from tkinter import filedialog

import database_core
from database_core import Database
import database_insert

# hints_for_types = {'date': ''}

root = Tk()
root.title('Import Random DB v1')
# root.iconbitmap("c:/vs.code/images/dice.ICO")
root.geometry('800x800')
root.grid_columnconfigure(0, weight=1)


def grid_buttons(buttons: list):
    col = 0
    for button in buttons:
        button.grid(row=0, column=col, ipadx=3, ipady=3, padx=5, pady=5)
        col += 1


def open_db():
    clear()
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
    clear()
    global is_open
    if is_open:
        global db
        del db
        is_open = False
        # navbar_frame.grid_slaves(row=1, column=0)[0].grid_remove()
        global open_label_text
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


def update_open_label():
    global open_label
    global open_label_text
    open_label.config(text=open_label_text, fg='black')


def create():
    clear()
    # add the create method ui
    # add hints for available types
    pass


def insert():
    def add_to_db():
        values_list = [x.get() for x in list[Entry](insert_input_frame.grid_slaves(column=1))]
        values_list.reverse()
        print(str(database_insert.insert(db, values_list)))

    clear()
    if is_open:
        insert_master = Frame(root)
        insert_input_frame = Frame(insert_master)
        insert_input_frame.grid()
        button_row = 0
        for colon, i in zip(db.colons.keys(), range(len(db.colons))):
            Label(insert_input_frame, text=colon).grid(row=i, column=0, padx=3, pady=3, ipadx=3, ipady=3)
            Entry(insert_input_frame).grid(row=i, column=1, padx=3, pady=3, ipadx=3, ipady=3)
            Label(insert_input_frame, text=db.colons.get(colon)).grid(row=i, column=2, padx=3, pady=3, ipadx=3, ipady=3)
            button_row += 1
        Button(insert_master, text='Add', width=10, bg='green', fg='white', command=add_to_db).grid(row=button_row,
                                                                                                    column=0, padx=3,
                                                                                                    pady=3, ipadx=3,
                                                                                                    ipady=3)
        insert_master.grid(row=1, sticky='NW')


def clear():
    for widget in root.grid_slaves(row=1):
        widget.grid_forget()


def error_handler(errors: list):
    # add new frame in root (row=1, column=1)
    # display errors in there
    pass


global db
is_open = False
open_label_text = 'No database currently open.'

navbar_frame = Frame(root, relief=RAISED, bd=3)
navbar_frame.grid(row=0, column=0, sticky='new')
open_label = Label(navbar_frame, text=open_label_text)
open_label.grid(row=1, column=0, ipadx=3, ipady=3,
                padx=5, pady=5,
                columnspan=3)

navbar_buttons = [
    Button(navbar_frame,
           text="open", command=open_db),
    Button(navbar_frame, text="close", command=close),
    Button(navbar_frame, text="drop", command=drop),
    Button(navbar_frame, text="create", command=create),
    Button(navbar_frame, text="insert", command=insert),
    Button(navbar_frame, text="select"),
    Button(navbar_frame, text="Exit", command=root.destroy)
]

grid_buttons(navbar_buttons)

root.mainloop()
