from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile, askopenfilename
import os
import pygame
import json

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
    update_edit_pane()

def add_cue():
    f = askopenfilename(filetypes=[("All Files", "*.*"), ("MP3 File", "*.mp3"), ("WAV File", "*.wav")])
    files.append({"Title": os.path.basename(f), "path": f})
    build_cue_list(files)

def build_cue_list(json):
    global files
    files = json
    lb.delete(0, END)
    for id, x in enumerate(files):
        lb.insert(id, x["Title"])
    lb.activate(0)
    lb.selection_set(0)

def update_edit_pane():
    selection = lb.curselection()
    cue_name_entry.delete(0, END)
    path_entry.delete(0, END)
    if selection:
        cue = files[selection[0]]
        cue_name_entry.insert(0, cue["Title"])
        path_entry.insert(0, cue["path"])

def update_edit_pane_bind(e):
    update_edit_pane()

def save_cue_edit():
    selection = lb.curselection()
    if selection:
        files[selection[0]]["Title"] = cue_name_entry.get()
        files[selection[0]]["path"] = path_entry.get()
        build_cue_list(files)
        lb.select_clear(0, END)
        lb.activate(selection[0])
        lb.selection_set(selection[0])

pygame.mixer.init()
root = Tk()
root.title("Sound Cue Manager")
root.geometry("700x300")

main_pane = PanedWindow()
main_pane.grid();

cue_list_pane = PanedWindow(main_pane, orient=VERTICAL)
controls_pane = PanedWindow(main_pane)
edit_pane = PanedWindow(main_pane, orient=VERTICAL)

main_pane.add(cue_list_pane)
main_pane.add(controls_pane)
main_pane.add(edit_pane)

edit_title_label = Label(edit_pane, anchor="nw", text="Edit Cue")
Label(edit_pane, text="Cue Label:").grid(row=0, column=0)
cue_name_entry = Entry(edit_pane)
cue_name_entry.grid(row=0, column=1)
Label(edit_pane, text="Path:").grid(row=1, column=0)
path_entry = Entry(edit_pane)
path_entry.grid(row=1, column=1)
ttk.Button(edit_pane, text="Save", command=save_cue_edit).grid(row=2, column=0)

lb = Listbox(cue_list_pane)
lb.grid(column=0, row=0, rowspan=3, padx=5, pady=5, sticky='nsew')
cue_list_pane.add(lb)

files = []

playBtn = ttk.Button(controls_pane, text="Play", command=play)
lb.bind("<KeyPress>", checkKey)
lb.bind("<<ListboxSelect>>", update_edit_pane_bind)
playBtn.grid(column=0, row=0)
ttk.Button(controls_pane, text="Stop", command=stop).grid(column=1, row=0)
ttk.Button(controls_pane, text="Previous", command=prevCue).grid(column=0, row=1)
ttk.Button(controls_pane, text="Next", command=nextCue).grid(column=1, row=1)
ttk.Button(controls_pane, text="Quit", command=root.destroy).grid(column=0, row=3)
ttk.Button(controls_pane, text="Save", command=lambda:save_file()).grid(column=0, row=4)
ttk.Button(controls_pane, text="Load", command=lambda:open_file()).grid(column=0, row=5)
ttk.Button(controls_pane, text="Add Cue", command=lambda:add_cue()).grid(column=0, row=6)

root.mainloop()