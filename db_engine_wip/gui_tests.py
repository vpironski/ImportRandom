import os
from tkinter import *
from tkinter import filedialog

import database_core
from database_core import Database

root = Tk()
frame = Frame(root)
frame.grid(row=1, column=0)
root.title('Import Random DB v1')
# root.iconbitmap("c:/vs.code/images/dice.ICO")
root.geometry('800x800')
global db
is_open = False
open_label_text = 'No database currently open.'


def open_db():
    filename = filedialog.askopenfilename(initialdir=os.getcwd() + '/Databases', title='Select a database',
                                          filetypes=(('databases', database_core.file_extension),))
    global is_open
    global db
    is_open = True
    if not str(filename) == '':
        db = Database(filename)
        global open_label_text
        open_label_text = f'Currently open: {db.name}.'
        update_label()
    del filename


def close():
    global is_open
    if is_open:
        global db
        del db
        is_open = False
        # frame.grid_slaves(row=1, column=0)[0].grid_remove()
        global open_label_text
        open_label_text = 'No database is currently open.'
        update_label()


def drop():
    if is_open:
        db.drop()
        close()


def update_label():
    root.grid_slaves(row=0)[0].grid_forget()
    Label(root, text=open_label_text).grid(row=0, column=0, ipadx=3, ipady=3, columnspan=3)
    print(root.grid_slaves(row=0))


Label(root, text=open_label_text).grid(row=0, column=0, ipadx=3, ipady=3, columnspan=3)

exit_button = Button(frame, text="Exit", command=root.destroy)
exit_button.grid(row=0, column=6)

b1_button = Button(frame, text="open", command=open_db)
b1_button.grid(row=0, column=0)

b2_button = Button(frame, text="close", command=close)
b2_button.grid(row=0, column=1)

b3_button = Button(frame, text="drop", command=drop)
b3_button.grid(row=0, column=2)

b4_button = Button(frame, text="create")
b4_button.grid(row=0, column=3)

b5_button = Button(frame, text="insert")
b5_button.grid(row=0, column=4)

b6_button = Button(frame, text="select")
b6_button.grid(row=0, column=5)

root.mainloop()
