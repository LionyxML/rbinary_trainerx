#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk


show_binary = 0


def quit():
    root.destroy()


def sobre():
    mb.showinfo("rx-binary_trainer", '''

    rx-binary_trainer

    Helps you learn binary representation intuitively.

    Version: 0.2

    Author : Rahul M. Juliato
             rahuljuliato.com

''')


def calc(value):
    value = sca_bit7.get() * 2**7 +\
            sca_bit6.get() * 2**6 +\
            sca_bit5.get() * 2**5 +\
            sca_bit4.get() * 2**4 +\
            sca_bit3.get() * 2**3 +\
            sca_bit2.get() * 2**2 +\
            sca_bit1.get() * 2**1 +\
            sca_bit0.get() * 2**0

    ent_answer.config(state="normal")
    ent_answer.delete(0, 100)
    ent_answer.insert(0, str(value))
    ent_answer.config(state="readonly")


root = tk.Tk()
root.wm_title('rx-binary_trainer v0.2')
root.wm_minsize(400, 220)
root.grid_anchor(anchor='c')

barramenu = tk.Menu(root)
file_menu = tk.Menu(barramenu, tearoff=800)
file_menu.add_command(label="About", command=sobre)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
barramenu.add_cascade(label="File", menu=file_menu)

root.config(menu=barramenu)

ent_answer = tk.Entry(root, justify="center", font=("TkFixedFont", 24),
                      state="readonly")
ent_answer.grid(row=0, column=0, columnspan=8, pady=20)

sca_bit7 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit7.grid(row=1, column=0)

sca_bit6 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit6.grid(row=1, column=1)

sca_bit5 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit5.grid(row=1, column=2)

sca_bit4 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit4.grid(row=1, column=3)

sca_bit3 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit3.grid(row=1, column=4)

sca_bit2 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit2.grid(row=1, column=5)

sca_bit1 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit1.grid(row=1, column=6)

sca_bit0 = tk.Scale(root, orient="vertical", from_=1, to=0,
                    showvalue=show_binary, command=calc)
sca_bit0.grid(row=1, column=7)

root.mainloop()
