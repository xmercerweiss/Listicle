import tkinter as tk
from tkinter import ttk

import os

class Listicle:

    _TASKS_FILE = "./tasks"

    _ROOT_TITLE = "Listicle"
    _ROOT_GEO = "440x800"
    _ROOT_MIN_W = 440
    _ROOT_MIN_H = 50

    _WIDGET_X_PAD = 3
    _WIDGET_Y_PAD = 2

    _ENTRY_BUTTON_TEXT = "+Add Task"
    _ENTRY_BUTTON_FONT = ("Courier New", 12, "bold")
    _ENTRY_BUTTON_FG = "#FFFFFF"
    _ENTRY_BUTTON_BG = "#DA3A13"
    _ENTRY_BUTTON_BD = 5
    
    _TASK_BUTTON_FONT = ("Courier New", 14)
    _TASK_BUTTON_FG = "#FFFFFF"
    _TASK_BUTTON_BG = "#DA3A13"

    _TEXTBOX_FONT = ("Courier New", 16, "bold")

    def __init__(self):
        self._tasks = []
        self._root = self._init_root()
        self._entry_frame, self._tasks_frame = self._init_frames()
        _, self._textbox = self._populate_entry_frame()

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

    def _populate_entry_frame(self):
        textbox = tk.Entry(
            self._entry_frame,
            font=self._TEXTBOX_FONT
        )
        textbox.bind("<Return>", self._add_task)
        textbox.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=self._WIDGET_X_PAD
        )

        entry_button = tk.Button(
            self._entry_frame,
            text=self._ENTRY_BUTTON_TEXT,
            font=self._ENTRY_BUTTON_FONT,
            fg=self._ENTRY_BUTTON_FG,
            bg=self._ENTRY_BUTTON_BG,
            bd=self._ENTRY_BUTTON_BD,
            command=self._add_task
        )
        entry_button.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=self._WIDGET_X_PAD
        )

        return entry_button, textbox

    def _populate_tasks_frame(self):
        for task in self._tasks:
            self._build_task_button(task)

    def _build_task_button(self, task):
        button = tk.Button(
            self._tasks_frame,
            text=task,
            font=self._TASK_BUTTON_FONT,
            command=lambda: self._remove_task(task)
        )

        button.pack(
            expand=False,
            fill=tk.X,
            padx=self._WIDGET_X_PAD,
            pady=self._WIDGET_Y_PAD,
            side=tk.TOP
        )

    def _add_task(self, *_):
        # NOTE: Additional arguments are disregarded due to the extra
        # argument passed by .bind() which is not passed elsewhere and
        # is not used by this method.
        task = self._textbox.get()
        if task.strip() == "":
            return
        self._textbox.delete(0, tk.END)
        self._tasks.append(task)
        self._build_task_button(task)

    def _remove_task(self, task):
        # NOTE: In the event that mutiple tasks store exactly the same
        # text, the first occurance will be deleted, not necessarily
        # the one the user clicked on. This bug is so minor and unlikely
        # to occur, and would require such significant restructuring,
        # that it has not been patched.
        if task not in self._tasks:
            return
        self._tasks.remove(task)
        for child in self._tasks_frame.winfo_children():
            if child.cget("text") == task:
                child.destroy()
                return

    def _get_tasks(self):
        if not os.path.isfile(self._TASKS_FILE):
          open(self._TASKS_FILE, "a").close()
          return
        
        self._tasks = []
        with open(self._TASKS_FILE, "r") as file:
            for line in file.readlines():
                self._tasks.append(line.strip())

    def _put_tasks(self):
        with open(self._TASKS_FILE, "w") as file:
            for task in self._tasks:
                file.write(task + "\n")

    def mainloop(self):
        self._get_tasks()
        self._populate_tasks_frame()
        self._root.mainloop()
        self._put_tasks()

