import tkinter as tk
from tkinter import ttk


class Listicle:

    _ROOT_TITLE = "Listicle"
    _ROOT_GEO = "440x800"
    _ROOT_MIN_W = 440
    _ROOT_MIN_H = 100

    def __init__(self):
        self._root = self._init_root()
        self._entry_frame, self._tasks_frame = self._init_frames()
        self._populate_entry_frame()
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
        pass

    def _populate_tasks_frame(self):
        pass

    def mainloop(self):
        self._root.mainloop()

