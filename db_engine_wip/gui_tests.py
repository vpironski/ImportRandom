import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import database_core
from database_core import Database

root = Tk()
root.title('Database engine v1')
root.geometry('800x800')


def command_action(event):
    print(selection.get())
    if selection.get() == 'open':
        filename = filedialog.askopenfilename(initialdir=os.getcwd() + '/Databases', title='Select a database',
                                              filetypes=(('databases', database_core.file_extension),))
        db = Database(filename)
        open_label = Label(frame, text=f'Currently open: {db.name}')
        open_label.grid(row=0, column=1, padx=10, pady=10, ipadx=3, ipady=3)
        if selection.get() == 'close':

            del db



frame = Frame(root)
frame.grid(row=0, column=0, ipadx=5, ipady=5)
commands = ['open', 'close', 'drop', 'create', 'insert', 'select']
selection = StringVar()
selection.set('Select a command')
dropdown = OptionMenu(frame, selection, *commands, command=command_action)
dropdown.grid(row=0, column=0, padx=10, pady=10, ipadx=3, ipady=3,)
root.mainloop()
