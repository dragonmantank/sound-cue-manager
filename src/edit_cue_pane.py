import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font as tkFont

class EditCuePane:
    def __init__(self, app, parent):
        self.app = app
        helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')

        self.pane = tk.PanedWindow(parent, orient=tk.VERTICAL)
        edit_title_label = tk.Label(self.pane, font=helv36, anchor="nw", text="Edit Cue")
        tk.Label(self.pane,  font=helv36,text="Cue Label:").grid(row=0, column=0)
        self.cue_name_entry = tk.Entry(self.pane, font=helv36)
        self.cue_name_entry.grid(row=0, column=1)
        tk.Label(self.pane,  font=helv36,text="Path:").grid(row=1, column=0)
        self.path_entry = tk.Entry(self.pane, font=helv36)
        self.path_entry.grid(row=1, column=1)

        self.loop_var = tk.IntVar()
        # style = ttk.Style(self.app.root)
        # style.configure('TCheckbutton', font=helv36)
        # self.loop = ttk.Checkbutton(self.pane, style=style, text="Loop?", variable=self.loop_var, onvalue=1, offvalue=0)
        self.loop = tk.Checkbutton(self.pane, font=helv36, text="Loop?", variable=self.loop_var, onvalue=1, offvalue=0)
        self.loop.grid(row=2, column=0)

        tk.Button(self.pane, font=helv36, text="Save", command=self.save_cue_edit).grid(row=3, column=0)

    def save_cue_edit(self):
        selection = self.app.cue_list_pane.lb.curselection()
        if selection:
            self.app.files[selection[0]]["Title"] = self.cue_name_entry.get()
            self.app.files[selection[0]]["path"] = self.path_entry.get()
            self.app.files[selection[0]]["loop"] = self.loop_var.get()
            self.app.build_cue_list()
            self.app.cue_list_pane.lb.select_clear(0, tk.END)
            self.app.cue_list_pane.lb.activate(selection[0])
            self.app.cue_list_pane.lb.selection_set(selection[0])