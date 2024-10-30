import tkinter as tk
from tkinter import ttk


class Listicle:

    _ROOT_TITLE = "Listicle"
    _ROOT_GEO = "440x800"
    _ROOT_MIN_W = 440
    _ROOT_MIN_H = 50

    _WIDGET_X_PAD = 2

    _BUTTON_TEXT = "+Add Task"
    _BUTTON_FONT = ("Courier New", 12, "bold")
    _BUTTON_FG = "#FFFFFF"
    _BUTTON_BG = "#DA3A13"
    
    _TEXTBOX_FONT = ("Courier New", 16, "bold")

    def __init__(self):
        self._root = self._init_root()
        self._entry_frame, self._tasks_frame = self._init_frames()
        self._textbox = self._init_textbox()
        self._populate_tasks_frame()

    def _init_root(self):
        root = tk.Tk()
        root.title(self._ROOT_TITLE)
        root.geometry(self._ROOT_GEO)
        root.minsize(self._ROOT_MIN_W, self._ROOT_MIN_H)
        root.maxsize(self._ROOT_MIN_W, root.winfo_screenheight() - 1)
        root.resizable(width=False, height=True)
        return root

    def _init_frames(self):
        entry_frame = tk.Frame(
            self._root,
            height=self._ROOT_MIN_H
        )
        for i in range(3):
            entry_frame.rowconfigure(i, weight=1)
        entry_frame.columnconfigure(0, weight=4)
        entry_frame.columnconfigure(1, weight=1)
        entry_frame.grid_propagate(0)
        entry_frame.pack(
            expand=False,
            fill=tk.BOTH
        )
        
        sep = ttk.Separator(
            self._root, 
            orient=tk.HORIZONTAL
        )
        sep.pack(
            fill=tk.X
        )

        tasks_frame = tk.Frame(self._root)
        tasks_frame.pack(
            expand=True,
            fill=tk.BOTH
        )

        return entry_frame, tasks_frame

    def _init_textbox(self):
        textbox = tk.Entry(
            self._entry_frame,
            font=self._TEXTBOX_FONT
        )
        textbox.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=self._WIDGET_X_PAD
        )

        button = tk.Button(
            self._entry_frame,
            text=self._BUTTON_TEXT,
            font=self._BUTTON_FONT,
            fg=self._BUTTON_FG,
            bg=self._BUTTON_BG
        )
        button.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=self._WIDGET_X_PAD
        )

        return textbox

    def _populate_tasks_frame(self):
        pass

    def mainloop(self):
        self._root.mainloop()

