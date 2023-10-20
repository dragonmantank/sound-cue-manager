import tkinter as tk
import pygame
from tkinter.filedialog import asksaveasfile, askopenfile, askopenfilename
import json
import os

class ControlsPane:
    def __init__(self, app, parent):
        self.app = app

        self.pane = tk.PanedWindow(parent)
        tk.Button(self.pane, text="Play", command=self.play).grid(column=0, row=0)
        tk.Button(self.pane, text="Stop", command=self.stop).grid(column=1, row=0)
        tk.Button(self.pane, text="Previous", command=self.prevCue).grid(column=0, row=1)
        tk.Button(self.pane, text="Next", command=self.nextCue).grid(column=1, row=1)
        tk.Button(self.pane, text="Quit", command=app.root.destroy).grid(column=0, row=3)
        tk.Button(self.pane, text="Save", command=lambda:self.save_file()).grid(column=0, row=4)
        tk.Button(self.pane, text="Load", command=lambda:self.open_file()).grid(column=0, row=5)
        tk.Button(self.pane, text="Add Cue", command=lambda:self.add_cue()).grid(column=0, row=6)

    def play(self):
        selection = self.app.cue_list_pane.lb.curselection()
        if selection:
            file_info = self.app.files[selection[0]]
            pygame.mixer.music.load(file_info["path"])
            loop = (file_info['loop'] or 0) * 99
            pygame.mixer.music.play(loops=loop)
            self.nextCue()

    def stop(self):
        pygame.mixer.music.stop()

    def nextCue(self):
        selected = self.app.cue_list_pane.lb.curselection()
        last_selection = int(selected[-1])
        next_selection = last_selection + 1
        self.app.cue_list_pane.lb.select_clear(selected)
        self.app.cue_list_pane.lb.activate(next_selection)
        self.app.cue_list_pane.lb.selection_set(next_selection)

    def prevCue(self):
        selected = self.app.cue_list_pane.lb.curselection()
        last_selection = int(selected[-1])
        next_selection = last_selection - 1
        self.app.cue_list_pane.lb.select_clear(selected)
        self.app.cue_list_pane.lb.activate(next_selection)
        self.app.cue_list_pane.lb.selection_set(next_selection)

    def save_file(self):
        f = asksaveasfile(initialfile="cues.json", defaultextension=".json", filetypes=[("All Files", "*.*"), ("JSON File", "*.json")])
        f.write(json.dumps(self.app.files, indent=2))

    def open_file(self):
        f = askopenfile(initialfile="cues.json", defaultextension=".json", filetypes=[("All Files", "*.*"), ("JSON File", "*.json")])
        data = f.read()
        json_data = json.loads(data)
        self.app.files = json_data
        self.app.build_cue_list()
        self.app.update_edit_pane()

    def add_cue(self):
        f = askopenfilename(filetypes=[("All Files", "*.*"), ("MP3 File", "*.mp3"), ("WAV File", "*.wav")])
        self.app.files.append(
            {
                "Title": os.path.basename(f), 
                "path": f,
                "loop": 0
            }
        )
        self.app.build_cue_list()