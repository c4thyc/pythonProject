#where the program is ran

import tkinter as tk
from tkinter import ttk

#window
window  = tk.Tk()
window.title('Smart Budgeter')
window.geometry('700x500')

#title
titleLabel = ttk.Label(master = window, text = 'Smart Budgeter', font = ('Arial', 30))
titleLabel.pack(padx = 0, pady = 40)

#name
name = ttk.

#entry widget made
entry = tk.Entry(master = window)
entry.pack(padx = 0, pady = 70)

#text for entering the budgeting info (larger bodies of text)
#text = tk.Text(master = , height = , font = ('', fontsize))
#text.pack()

def getInput():
    userInput = entry.get()

#button
button = tk.Button(master = window, text = 'Enter', font = ('Arial', 18))
button.pack(padx = 0, pady = 0)

#run
window.mainloop()

#test