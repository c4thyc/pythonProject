#where the program is ran

import tkinter as tk
from tkinter import ttk

#window
window  = tk.Tk()
window.title('Smart Budgeter')
window.geometry('700x500')

#title
titleLabel = ttk.Label(master = window, text = 'ABC', font = 'Arial')
titleLabel.pack()

#entry widget made
entry = tk.Entry(window)
entry.pack()

def getInput():
    userInput = entry.get()

#button
button = tk.Button.get()
button.pack()

#run
window.mainloop()

#test