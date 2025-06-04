#where the program is run

import tkinter as tk
from tkinter import ttk
from dataHistory import save_user_info, load_user_info, save_monthly_data, load_monthly_data
from recommendation import recommendations_frame

#window
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Smart Budgeter')
        self.window.geometry('700x500')

        #for the grid
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        #loads existing data
        self.userData = load_user_info()

        #three frames
        self.nameFrame = tk.Frame(self.window)
        self.goalFrame = tk.Frame(self.window)
        self.mainAppFrame = tk.Frame(self.window)

        #layout of the window
        self.frames = {}
        for name in ("nameFrame", "goalFrame", "menuFrame", "budgetingFrame", "historyFrame", "recommendationsFrame"):
            frame = tk.Frame(self.window)
            frame.grid(row = 0, column = 0, sticky = 'nsew')
            self.frames[name] = frame

        self.name_frame()
        self.goal_frame()
        self.menu_frame()
        self.budgeting_frame()
        self.history_frame()
        recommendations_frame(self)

        #instantiates a new list to store the user data if there isn't already data stored (if user is new)
        if self.userData and "name" in self.userData:
            self.goalReminder.config(text = f"Goal: {self.userData.get('goal', '')}")
            self.new_frame("menuFrame")
        else:
            self.new_frame("nameFrame")

        self.window.mainloop()

    #after the user enters their name
    def new_frame(self, frameName):
        self.frames[frameName].tkraise()  #switches between frames (like from name frame to goal frame)

    def name_frame(self):
        #makes the frame for the list
        frame = self.frames["nameFrame"]

        #title page
        self.titleLabel = ttk.Label(master = frame, text = 'Smart Budgeter', font = ('Arial', 30))
        self.titleLabel.pack(padx = 210, pady = 30)

        #asks for username
        self.nameLabel = ttk.Label(master = frame, text = 'What is your name?', font = ('Arial', 14))
        self.nameLabel.pack(pady = 10)

        #textbox for the username
        self.nameEntry = ttk.Entry(master = frame, width = 30)
        self.nameEntry.pack(pady = 10)

        #button to enter name
        self.nameButton = ttk.Button(master = frame, text = 'Enter', command = self.personalize)
        self.nameButton.pack(pady = 20)

    def goal_frame(self):
        #makes frame for list
        frame = self.frames["goalFrame"]
        #questions about goal
        self.welcomeLabel = ttk.Label(master = frame, text = '', font = ('Arial', 30))
        self.welcomeLabel.pack(pady = 20)

        #question
        self.goalLabel = ttk.Label(master = frame, text = 'What is your budgeting goal?', font = ('Arial', 20))
        self.goalLabel.pack(pady = 5)

        #entry box for the goal
        self.goalEntry = ttk.Entry(master = frame, font = ('Arial', 20))
        self.goalEntry.pack(pady = 20)

        #button to go next to budgeting function
        self.personalizeButton = ttk.Button(master = frame, text = 'Next', command = self.goal_reminder)
        self.personalizeButton.pack(pady = 15)

    def menu_frame(self):
        frame = self.frames["menuFrame"]
        mainMenuTitle = ttk.Label(master = frame, text = 'Main Menu', font = ('Arial', 24))
        mainMenuTitle.pack(pady = 20)
        self.goalReminder = ttk.Label(master = frame, text = '', font = ('Arial', 14))
        self.goalReminder.pack(pady = 10)
        ttk.Button(master = frame, text = 'Monthly Budget', command = lambda: self.new_frame("budgetingFrame")).pack(pady = 10)
        ttk.Button(master = frame, text = 'Budget History', command = self.display_history).pack(pady = 10)
        ttk.Button(master = frame, text = 'Recommendations', command = self.to_recommendations).pack(pady = 10)

    def budgeting_frame(self):
        frame = self.frames["budgetingFrame"]

        #puts goal on top for reminder
        self.goalReminder = ttk.Label(master = frame, text = '', font = ('Arial', 14))
        self.goalReminder.pack(pady = 10)

        #enter data for each month
        self.monthLabel = ttk.Label(master = frame, text = 'Month:')
        self.monthLabel.pack()
        self.monthEntry = ttk.Entry(master = frame)
        self.monthEntry.pack(pady = 5)

        #enter data for monthly income
        self.incomeLabel = ttk.Label(master = frame, text = 'Monthly Income:')
        self.incomeLabel.pack()
        self.incomeEntry = ttk.Entry(master = frame)
        self.incomeEntry.pack(pady = 5)

        #enter data for savings
        self.savingsLabel = ttk.Label(master = frame, text = 'Savings:')
        self.savingsLabel.pack()
        self.savingsEntry = ttk.Entry(master = frame)
        self.savingsEntry.pack(pady = 5)

        #enter data for util (water, gas, electricity)
        self.utilLabel = ttk.Label(master = frame, text = 'Utilities:')
        self.utilLabel.pack()
        self.utilEntry = ttk.Entry(master = frame)
        self.utilEntry.pack(pady = 5)

        #enter data for cost of transportation (bus, car)
        self.tpLabel = ttk.Label(master = frame, text = 'Transportation:')
        self.tpLabel.pack()
        self.transportEntry = ttk.Entry(master = frame)
        self.transportEntry.pack(pady = 5)

        #button for entering the budget plan for the month
        self.submit_button = ttk.Button(master = frame, text = 'Save Month Plan', command = self.submit_month)
        self.submit_button.pack(pady = 10)

        #button for going back to the main menu
        self.mainButton = ttk.Button(master = frame, text = 'Back to Main Menu', command = lambda: self.new_frame("menuFrame"))
        self.mainButton.pack(pady = 10)

    def history_frame(self):
        frame = self.frames["historyFrame"]
        self.historyText = tk.Text(master = frame, height = 20, width = 80)
        self.historyText.pack(pady=10)
        ttk.Button(frame, text='Back to Menu', command = lambda: self.new_frame("menuFrame")).pack(pady=10)

    #keeps data about the goal of the user, to personalize their experience
    def personalize(self):
        name = self.nameEntry.get().strip()
        if name:
            if self.userData is None:
                self.userData = {}
            self.userData = load_user_info() or {}
            self.userData["name"] = name
            self.welcomeLabel.config(text = f"Welcome, {name}!")
            self.new_frame("goalFrame")

    #keeps goal on top
    def goal_reminder(self):
        goal = self.goalEntry.get().strip()

        if self.userData is None:
            self.userData = {}

        self.userData["goal"] = goal
        save_user_info(self.userData, goal)
        self.goalReminder.config(text = f"Goal: {goal}")
        self.frames["budgetingFrame"].children[self.goalReminder.winfo_name()].config(text = f"Goal: {goal}")
        self.new_frame("menuFrame")

    #links the data to the month and stores it
    def submit_month(self):
        month = self.monthEntry.get().strip()
        if not month:
            return
        #list for all the data for that month
        data = {
            'income': float(self.incomeEntry.get()),
            'savings': float(self.savingsEntry.get()),
            'utilities': float(self.utilEntry.get()),
            'transport': float(self.transportEntry.get())
        }
        save_monthly_data(month, data)  #saves it before it gets deleted
        self.monthEntry.delete(0, 'end')  #removes the data so new data can be entered
        self.incomeEntry.delete(0, 'end')
        self.savingsEntry.delete(0, 'end')
        self.utilEntry.delete(0, 'end')
        self.transportEntry.delete(0, 'end')

    def display_history(self):
        self.historyText.delete('1.0', tk.END)
        data = load_monthly_data(self)
        if not data:
            self.historyText.insert(tk.END, "No budgeting data found.\n")
        else:
            for month, details in data.items():
                self.historyText.insert(tk.END, f"{month}:\n")
                for key, value in details.items():
                    self.historyText.insert(tk.END, f"  {key}: ${value}\n")
                self.historyText.insert(tk.END, "\n")
        self.new_frame("historyFrame")

    def to_recommendations(self):
        self.new_frame("recommendationsFrame")

GUI()

#in order to restart the program and renew your data, you need to delete the user