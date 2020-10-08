from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog


def browsefunc_mp4(text):
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    text.insert(0, filename)


def browsefunc_dir(text):
    dir_name = filedialog.askdirectory(initialdir="/")
    text.insert(0, dir_name)


def browsefunc_txt(text):
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    text.insert(0, filename)


def create_block(name, window, command, column, row):
    lb = Label(window, text=name)
    lb.grid(column=column, row=row)

    text = Entry(window, width=30)
    text.grid(column=column+1, row=row)
    btn = Button(window, text="Browse", command=lambda: command(text))
    btn.grid(column=column+2, row=row)
    return text


def create_cut_button(name, window, command, text_1, text_2, text_3):
    btn = Button(window, text=name, fg="red", command=lambda: command(text_1, text_2, text_3, window))
    btn.grid(column=1, row=4)


def create_progress_bar(window):
    progress_bar = ttk.Progressbar(window, orient="horizontal",
                                   mode="determinate", maximum=100, value=0, length=190)
    progress_bar.grid(column=1, row=6)
    window.update()
    progress_bar['value'] = 0
    return progress_bar


def progress_bar_move(progress_bar, n):
    progress_bar['value'] += 100 / (int(n) - 1)

def end_msg():
    mb = messagebox.showinfo(title='End', message="Стрим порезан")
