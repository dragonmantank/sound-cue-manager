import tkinter as tk

class CueListPane:
    def __init__(self, app, parent):
        self.app = app

        self.pane = tk.PanedWindow(parent, orient=tk.VERTICAL)
        self.lb = tk.Listbox(self.pane)

        self.lb.grid(row=0, column=0, rowspan=3, padx=5, pady=5, sticky='nsew')
        self.lb.bind("<<ListboxSelect>>", self.update_edit_pane_bind)
        self.lb.bind("<KeyPress>", self.checkKey)

    def update_edit_pane_bind(self, e):
        self.app.update_edit_pane()

    def checkKey(self,e):
        if e.char == " ":
            self.app.controls_pane.play()
