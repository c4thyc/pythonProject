#where the program is ran

"""""
import tkinter as tk
from tkinter import ttk

#window gui
window = tk.Tk()
window.title('Smart Budgeter')
window.geometry('700x500')

#title
titleLabel = ttk.Label(master = window, text = 'Smart Budgeter', font = ('Arial', 30))
titleLabel.pack(padx = 0, pady = 20)

#name
#name = ttk.

#enter income
income_entry = tk.Entry(window)
income_entry.pack(pady = 10)

window.mainloop()

##entry = tk.Entry(master = window)
## entry.pack(padx = 0, pady = 70)

#text for entering the budgeting info (larger bodies of text)
#text = tk.Text(master = , height = , font = ('', fontsize))
#text.pack()

## def getInput():
    ##userInput = entry.get()

#button
##button = tk.Button(master = window, text = 'Enter', font = ('Arial', 18))
##button.pack(padx = 0, pady = 0)

#run
##window.mainloop()

#test

"""

import tkinter as tk
from tkinter import ttk
from dataHistory import save_user_info, load_user_info, save_monthly_data

#window
window = tk.Tk()
window.title('Smart Budgeter')
window.geometry('700x500')

userData = load_user_info()  #loads existing data

#start
nameFrame = tk.Frame(window)
personalizeFrame = tk.Frame(window)
mainAppFrame = tk.Frame(window)

#layout of the window
for frame in (nameFrame, personalizeFrame, mainAppFrame):
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#title page
titleLabel = ttk.Label(master = nameFrame , text = 'Smart Budgeter', font = ('Arial', 30))
titleLabel.pack(padx = 210, pady = 30)

#asks for username
nameLabel = ttk.Label(master = nameFrame, text = 'What is your name?', font = ('Arial', 14))
nameLabel.pack(pady = 10)

#textbox for the username
nameEntry = ttk.Entry(master = nameFrame, width = 30)
nameEntry.pack(pady = 10)

#instantiates a new list to store the user data if there isn't already data stored (if user is new)
if userData is None:
    userData = {}

#keeps data about the goal of the user, to personalize their experience
def personalize():
    name = nameEntry.get().strip()
    if name:
        userData['name'] = name
        welcomeLabel.config(text =f"Welcome, {name}!")
        showFrame(personalizeFrame)

#button to enter name
nameButton = ttk.Button(master = nameFrame, text ='Enter', command = personalize)
nameButton.pack(pady = 20)

#questions about goal
welcomeLabel = ttk.Label(master = personalizeFrame, text ='', font = ('Arial', 30))
welcomeLabel.pack(pady = 20)

#question
goalLabel = ttk.Label(master = personalizeFrame, text ='What is your budgeting goal?', font = ('Arial', 20))
goalLabel.pack(pady = 5)

#entry box for the goal
goalEntry = ttk.Entry(master = personalizeFrame, font = ('Arial', 20))
goalEntry.pack(pady = 20)

#keeps goal on top
def go_to_main():
    goal = goalEntry.get().strip()
    userData['goal'] = goal
    save_user_info(userData, goal)
    goalReminder.config(text =f"Goal: {goal}")
    showFrame(mainAppFrame)

#button to go next to budgeting function
personalizeButton = tk.Button(master = personalizeFrame, text = 'Start Budgeting', font = ('Arial', 10), command = go_to_main)
personalizeButton.pack(pady = 15)

#puts goal on top for reminder
goalReminder = ttk.Label(master = mainAppFrame, text ='', font = ('Arial', 14))
goalReminder.pack(pady = 10)

#enter data for each month
monthLabel = ttk.Label(master = mainAppFrame, text ='Month:')
monthLabel.pack()
monthEntry = ttk.Entry(master = mainAppFrame)
monthEntry.pack(pady = 5)

#enter data for monthly income
incomeLabel = ttk.Label(master = mainAppFrame, text ='Monthly Income:')
incomeLabel.pack()
incomeEntry = ttk.Entry(master = mainAppFrame)
incomeEntry.pack(pady = 5)

#enter data for savings
savingsLabel = ttk.Label(master = mainAppFrame, text ='Savings:')
savingsLabel.pack()
savingsEntry = ttk.Entry(master = mainAppFrame)
savingsEntry.pack(pady = 5)

#enter data for util (water, gas, electricity)
utilLabel = ttk.Label(master = mainAppFrame, text ='Utilities:')
utilLabel.pack()
utilEntry = ttk.Entry(master = mainAppFrame)
utilEntry.pack(pady = 5)

#enter data for cost of transportation (bus, car)
tpLabel = ttk.Label(master = mainAppFrame, text ='Transportation:')
tpLabel.pack()
transportEntry = ttk.Entry(master = mainAppFrame)
transportEntry.pack(pady = 5)

#links the data to the month and stores it
def submit_month():
    month = monthEntry.get().strip()
    if not month:
        return
    #list for all the data for that month
    data = {
        'income': float(incomeEntry.get()),
        'savings': float(savingsEntry.get()),
        'utilities': float(utilEntry.get()),
        'transport': float(transportEntry.get())
    }
    save_monthly_data(month, data) #saves it before it gets deleted
    monthEntry.delete(0, 'end') #removes the data so new data can be entered
    incomeEntry.delete(0, 'end')
    savingsEntry.delete(0, 'end')
    utilEntry.delete(0, 'end')
    transportEntry.delete(0, 'end')

#button for entering the budget plan for the month
submit_button = ttk.Button(master = mainAppFrame, text = 'Save Month Plan', command = submit_month)
submit_button.pack(pady = 10)

#frame---------

def showFrame(frame):
    frame.tkraise() #switches between frames (like from name frame to goal frame)

#after the user enters their name
if userData and "name" in userData:
    welcomeLabel.config(text =f"Welcome, {userData['name']}!")
    goalReminder.config(text =f"Goal: {userData.get('goal', '')}")
    showFrame(mainAppFrame)
else:
    showFrame(nameFrame)

#runs the code
window.mainloop()

#in order to restart the program and renew your data, you need to delete the user