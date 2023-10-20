import tkinter as tk

class EditCuePane:
    def __init__(self, app, parent):
        self.app = app

        self.pane = tk.PanedWindow(parent, orient=tk.VERTICAL)
        edit_title_label = tk.Label(self.pane, anchor="nw", text="Edit Cue")
        tk.Label(self.pane, text="Cue Label:").grid(row=0, column=0)
        self.cue_name_entry = tk.Entry(self.pane)
        self.cue_name_entry.grid(row=0, column=1)
        tk.Label(self.pane, text="Path:").grid(row=1, column=0)
        self.path_entry = tk.Entry(self.pane)
        self.path_entry.grid(row=1, column=1)
        tk.Button(self.pane, text="Save", command=self.save_cue_edit).grid(row=2, column=0)

    def save_cue_edit(self):
        selection = self.app.cue_list_pane.lb.curselection()
        if selection:
            self.app.files[selection[0]]["Title"] = self.cue_name_entry.get()
            self.app.files[selection[0]]["path"] = self.path_entry.get()
            self.app.build_cue_list()
            self.app.cue_list_pane.lb.select_clear(0, tk.END)
            self.app.cue_list_pane.lb.activate(selection[0])
            self.app.cue_list_pane.lb.selection_set(selection[0])