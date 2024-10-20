import tkinter as tk
import pygame
from .cue_list_pane import CueListPane
from .controls_pane import ControlsPane
from .edit_cue_pane import EditCuePane

class SoundCueManager:
    def __init__(self):
        pygame.mixer.init()

        self.root = tk.Tk()
        self.root.title("Sound Cue Manager")
        self.root.geometry("700x300")

        self.files = []

        self.setup_ui()

    def setup_ui(self):
        self.main_pane = tk.PanedWindow(self.root)
        self.main_pane.grid()

        self.cue_list_pane = CueListPane(self, self.main_pane)
        self.controls_pane = ControlsPane(self, self.main_pane)
        self.edit_pane = EditCuePane(self, self.main_pane)

        self.main_pane.add(self.cue_list_pane.pane)
        self.main_pane.add(self.controls_pane.pane)
        self.main_pane.add(self.edit_pane.pane)

    def build_cue_list(self):
        self.cue_list_pane.lb.delete(0, tk.END)
        for id, x in enumerate(self.files):
            title = x["Title"]
            loop = (x["loop"] or False)
            if loop:
                title = "(L)" + title
            self.cue_list_pane.lb.insert(id, title)
        self.cue_list_pane.lb.activate(0)
        self.cue_list_pane.lb.selection_set(0)

    def update_edit_pane(self):
        selection = self.cue_list_pane.lb.curselection()
        self.edit_pane.cue_name_entry.delete(0, tk.END)
        self.edit_pane.path_entry.delete(0, tk.END)
        if selection:
            cue = self.files[selection[0]]
            self.edit_pane.cue_name_entry.insert(0, cue["Title"])
            self.edit_pane.path_entry.insert(0, cue["path"])
            self.edit_pane.loop_var.set(cue["loop"])