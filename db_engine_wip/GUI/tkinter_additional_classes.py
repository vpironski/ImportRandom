import tkinter as tk
import platform


class ScrollFrame(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)  # create a frame (self)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # place canvas on self
        self.canvas = tk.Canvas(self, borderwidth=2)
        # place a frame on the canvas, this frame will hold the child widgets
        self.viewPort = tk.Frame(self.canvas)
        # place a scrollbar on self
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        # attach scrollbar action to scroll of canvas
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.grid(row=0, column=1, sticky='nsw')
        self.canvas.grid(row=0, column=0, sticky='nsew')
        # add view port frame to canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.viewPort, anchor="nw",
                                                       tags="self.viewPort")

        # bind an event whenever the size of the viewPort frame changes.
        self.viewPort.bind("<Configure>", self.on_frame_configure)
        # bind an event whenever the size of the canvas frame changes.
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # bind wheel events when the cursor enters the control
        self.viewPort.bind('<Enter>', self.on_enter)
        # unbind wheel events when the cursor leaves the viewPort frame
        self.viewPort.bind('<Leave>', self.on_leave)

        # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
        self.on_frame_configure(None)

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame.
        Whenever the size of the frame changes, alter the scroll region respectively."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        """Reset the canvas window to encompass inner frame when required
        Whenever the size of the canvas changes alter the window region respectively."""
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def on_mouse_wheel(self, event):  # cross-platform scroll wheel event
        if platform.system() == 'Windows':
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == 'Darwin':
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

    def on_enter(self, event):  # bind wheel events when the cursor enters the control
        if platform.system() == 'Linux':
            self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)
            self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_leave(self, event):  # unbind wheel events when the cursor leaves the viewPort frame
        if platform.system() == 'Linux':
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")


class SelectTable(ScrollFrame):
    def __init__(self, master, columns: dict, **kw):
        super().__init__(master, **kw)

        self.tBody = self.viewPort
        self.columns = columns
        self.rows = 1
        self.checkBoxes = list()

        for column, length, index in zip(columns.keys(), columns.values(), range(len(columns))):
            self.tBody.columnconfigure(index, weight=length)

        self.fill_head()

    def fill_head(self):
        for column, index in zip(self.columns.keys(), range(len(self.columns))):
            tk.Label(self.tBody, text=str(column).replace('_', ' '), relief=tk.SOLID, bd=2, bg='#fefefe',
                     font=("Segoe UI", 12, 'bold')) \
                .grid(row=0, column=index, sticky='nsew', ipadx=3, ipady=10)

    def add_row(self, values: list):
        self.checkBoxes.append(tk.IntVar(self.tBody, value=0))
        color = '#fafafa' if self.rows % 2 == 0 else '#e0e0e0'
        for i in range(len(self.columns) - 1):
            tk.Label(self.tBody, text=values[i], relief=tk.SOLID, bd=1, bg=color) \
                .grid(row=self.rows, column=i, sticky='nsew')
        tk.Checkbutton(self.tBody, variable=self.checkBoxes[-1], bg=color, relief=tk.SOLID, bd=1) \
            .grid(row=self.rows, column=len(self.columns) - 1, sticky='nsew')
        self.rows += 1

    def read_selected(self):
        for i in range(self.rows - 1):
            if self.checkBoxes[i].get() == 1:
                yield int(self.tBody.grid_slaves(row=i + 1)[-1]['text'])


class TableInputFrame(tk.Frame):
    def __init__(self, master, columns: dict, **kw):
        super().__init__(master, **kw)

        grid_column = 0
        grid_row = 0
        colon_names_list = list(columns.keys())[2:]
        for colon in colon_names_list:
            tk.Label(self, text=colon) \
                .grid(row=grid_row, column=grid_column, padx=3, pady=3, ipadx=3, ipady=3)
            tk.Entry(self).grid(row=grid_row, column=grid_column + 1, ipadx=3, ipady=3)
            tk.Label(self, text=columns.get(colon)) \
                .grid(row=grid_row, column=grid_column + 2, padx=3, pady=3, ipadx=3, ipady=3)
            grid_row += 1
            if grid_row == 20:
                grid_row = 0
                grid_column += 3

    def read_input(self):
        inputs = dict()
        for val, label in zip(list[tk.Entry](self.grid_slaves(column=1)
                                             + self.grid_slaves(column=4)
                                             + self.grid_slaves(column=7))[::-1],
                              list[tk.Label](self.grid_slaves(column=0)
                                             + self.grid_slaves(column=3)
                                             + self.grid_slaves(column=6))[::-1]):
            if not val.get() == '':
                inputs.update({label['text']: val.get()})
        return inputs
