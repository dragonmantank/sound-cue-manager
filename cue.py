from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from playsound import playsound
import pygame
import json

pygame.mixer.init()
root = Tk()
root.title = "Sound Cue Manager"
root.geometry("500x300")

main_pane = PanedWindow()
main_pane.grid();

cue_list_pane = PanedWindow(main_pane, orient=VERTICAL)
controls_pane = PanedWindow(main_pane)

main_pane.add(cue_list_pane)
main_pane.add(controls_pane)

lb = Listbox(cue_list_pane)
lb.grid(column=0, row=0, rowspan=3, padx=5, pady=5, sticky='nsew')
cue_list_pane.add(lb)

files = []

def play():
    global files
    pygame.mixer.music.load(files[lb.curselection()[0]]["path"])
    pygame.mixer.music.play()
    nextCue()

def nextCue():
    selected = lb.curselection()
    last_selection = int(selected[-1])
    next_selection = last_selection + 1
    lb.select_clear(selected)
    lb.activate(next_selection)
    lb.selection_set(next_selection)

def prevCue():
    selected = lb.curselection()
    last_selection = int(selected[-1])
    next_selection = last_selection - 1
    lb.select_clear(selected)
    lb.activate(next_selection)
    lb.selection_set(next_selection)

def stop():
    pygame.mixer.music.stop()

def checkKey(e):
    if e.char == " ":
        play()

def save_file():
    f = asksaveasfile(initialfile="cues.json", defaultextension=".json", filetypes=[("All Files", "*.*"), ("JSON File", "*.json")])
    f.write(json.dumps(files, indent=2))

def open_file():
    f = askopenfile(initialfile="cues.json", defaultextension=".json", filetypes=[("All Files", "*.*"), ("JSON File", "*.json")])
    data = f.read()
    json_data = json.loads(data)
    build_cue_list(json_data)

def build_cue_list(json):
    global files
    files = json
    for id, x in enumerate(files):
        lb.insert(id, x["Title"])
    lb.activate(0)
    lb.selection_set(0)

playBtn = ttk.Button(controls_pane, text="Play", command=play)
lb.bind("<KeyPress>", checkKey)
playBtn.grid(column=0, row=0)
ttk.Button(controls_pane, text="Stop", command=stop).grid(column=0, row=1)
ttk.Button(controls_pane, text="Previous", command=prevCue).grid(column=1, row=0)
ttk.Button(controls_pane, text="Next", command=nextCue).grid(column=1, row=1)
ttk.Button(controls_pane, text="Quit", command=root.destroy).grid(column=0, row=3)
ttk.Button(controls_pane, text="Save", command=lambda:save_file()).grid(column=0, row=4)
ttk.Button(controls_pane, text="Load", command=lambda:open_file()).grid(column=0, row=5)

root.mainloop()