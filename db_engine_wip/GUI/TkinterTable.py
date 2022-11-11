from tkinter import Frame


class DisplayTable(Frame):
    tHead = None
    tBody = None
    columns = 0

    def __init__(self, master, column_list: list, **kw):
        super().__init__(master, **kw)
        self.tHead = Frame(self)
