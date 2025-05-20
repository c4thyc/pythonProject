import tkinter as tk
from tkinter import ttk

#window
window  = tk.Tk()
window.title('Test')
window.geometry('500x800')

#title
titleLabel = ttk.Label(master = window, text = 'A', font = 'Arial')
titleLabel.pack()

#run
window.mainloop()