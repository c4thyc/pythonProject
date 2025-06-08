# code for budgeting program

import tkinter as tk # GUI
from tkinter import ttk
from dataHistory import save_user_info, load_user_info, save_monthly_data, load_monthly_data
from recommendation import recommendations_frame

class GUI:

    # initializing frame
    def __init__(self, *args, **kwargs):

        # window for the entire program
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window.title("Smart Budgeter")
        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)

        # list of all the frames (saves space)
        self.frames = {}
        for frame in (NameFrame, GoalFrame, MenuFrame, BudgetFrame, HistoryFrame, RecFrame):
            window = frame(self.window, self)
            window.grid(row = 0, column = 0, sticky = "nsew")
            self.frames[frame] = window

    # switches between frames
    def show_frame(self, frame):
        intendedFrame = self.frames[frame]
        intendedFrame.tkraise()

    # personalizes experience, keeps goal
    def personalize(self):
        name = self.nameEntry.get().strip()
        if name:
            if self.userData is None:
                self.userData = {}
            self.userData = load_user_info() or {}
            self.userData["name"] = name
            self.welcomeLabel.config(text = f"Welcome, {name}!")
            self.new_frame("goalFrame")

    # puts goal on the screen as a reminder
    def goal_reminder(self):
        goal = self.goalEntry.get().strip()

        if self.userData is None:
            self.userData = {}

        self.userData["goal"] = goal
        save_user_info(self.userData, goal)
        self.goalReminder.config(text=f"Goal: {goal}")
        self.frames["budgetingFrame"].children[self.goalReminder.winfo_name()].config(text=f"Goal: {goal}")
        self.new_frame("menuFrame")

    def to_recommendations(self):
        self.new_frame("recommendationsFrame")

# frame where user enters name
class NameFrame(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        # title of frame
        ttk.Label(master = self, text = "Smart Budgeter", font = ("Times New Roman", 30)).pack(padx = 210, pady = 30)
        # asks user to enter name, stores it in a variable
        self.nameEntry = ttk.Label(master = self, text = "Enter your name", font = ("Times New Roman", 14))
        self.nameEntry.pack(pady = 10)
        # name box
        ttk.Entry(master = self, font = ("Times New Roman", 10), width = 40).pack(pady = 10)
        # button to go next
        tk.Button(master = self, font = ("Times New Roman", 10), text = "Enter", command = lambda: controller.show_frame(GoalFrame))

# frame where user enters goal, personalization
class GoalFrame(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        # title of frame
        ttk.Label(master = self, text = "", font = ("Times New Roman", 30)).pack(pady = 20)
        # question about goal, stores goal into variable
        self.goalEntry = ttk.Label(master = self, text = "What is your budgeting goal?", font = ("Arial", 20))
        self.goalEntry.pack(pady = 5)
        # entry box for the goal
        ttk.Entry(master = self, font = ("Times New Roman", 20)).pack(pady = 20)
        # button to go next to budgeting function
        ttk.Button(master = self, text = "Enter", command = lambda: controller.show_frame(MenuFrame)).pack(pady = 15)

# frame where user can navigate to other frames
class MenuFrame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        # title of menu
        ttk.Label(master = self, text = "Main Menu", font = ("Times New Roman", 24)).pack(pady = 20)
        # budgeting tool
        ttk.Button(master = self, text = "Monthly Budget", command = lambda: controller.show_Frame(BudgetFrame)).pack(pady = 10)
        # budgeting history
        ttk.Button(master = self, text = "Budget History", command = lambda: controller.display_history).pack(pady = 10)
        # recommendations
        ttk.Button(master = self, text = "Recommendations", command = lambda: controller.to_recommendations).pack(pady = 10)

# frame where user budgets at a monthly rate
class BudgetFrame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        # puts goal on top for reminder
        ttk.Label(master = self, text = "", font = ("Times New Roman", 14)).pack(pady = 10)

        # to enter each month
        ttk.Label(master = self, text = "Month:").pack()
        self.monthEntry = ttk.Entry(master = self)
        self.monthEntry.pack(pady = 5)
        # to enter monthly income (job, allowance, lottery, investments, etc.)
        ttk.Label(master = self, text = "Monthly Income:").pack()
        self.incomeEntry = ttk.Entry(master = self)
        self.incomeEntry.pack(pady = 5)
        # to enter spending for food (groceries, restaurant, etc.)
        ttk.Label(master = self, text = "Food:").pack()
        self.foodEntry = ttk.Entry(master = self)
        self.foodEntry.pack(pady = 10)
        # to enter sending for housing and util (rent, water, gas, electricity, etc.)
        ttk.Label(master = self, text = "Housing/Utility:").pack()
        self.utilEntry = ttk.Entry(master = self)
        self.utilEntry.pack(pady = 5)
        # to enter spending for cost of transportation (bus, car, scooter, etc.)
        ttk.Label(master = self, text = "Transportation:").pack()
        self.transportEntry = ttk.Entry(master = self)
        self.transportEntry.pack(pady = 5)
        # to enter spending for personal/lifestyle (entertainment, gym, pets, clothes, etc.)
        ttk.Label(master = self, text = "Personal/Lifestyle:").pack()
        self.personalEntry = ttk.Entry(master = self)
        self.personalEntry.pack(pady = 5)
        # to enter savings
        ttk.Label(master = self, text = "Savings:").pack()
        self.savingsEntry = ttk.Entry(master = self)
        self.savingsEntry.pack(pady = 5)

        # button for entering the entire budget plan for the month
        ttk.Button(master = self, text = "Save Month Plan", command = controller.submit_month).pack(pady = 10)

        # button for going back to the main menu
        ttk.Button(master = self, text = "Back to Main Menu", command = lambda: controller.show_frame(MenuFrame)).pack(pady = 10)

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

# frame where user can view their budgeting history if applicable
class HistoryFrame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        self.historyText = tk.Text(master = self, height = 20, width = 80)
        self.historyText.pack(pady = 10)
        ttk.Button(master = self, text = "Back to Main Menu", command = lambda: controller.show_frame(MenuFrame)).pack(pady = 10)

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
        self.show_frame(HistoryFrame)

# frame where user can view budgeting recommendations (50/30/20)
class RecFrame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)

        # displays the rec info
        recommendations = """
            Recommended Budgeting Rule (50/30/20):

            - 50% Needs: rent, bills, groceries, transportation, etc.
            - 30% Wants: entertainment, hobbies, shopping, clothes, etc.
            - 20% Savings: savings account, investing, emergency fund, etc.
            """
        ttk.Label(master = self, text = "Recommendations", font = ("Times New Roman", 18)).pack(pady = 10)
        tk.Label(master = self, text = recommendations, font = ("Times New Roman", 14), justify = "left").pack(padx = 20)
        ttk.Button(master = self, text = "Back to Main Menu", command = lambda: controller.show_frame(MenuFrame)).pack(pady = 10)

# runs the program
program = GUI()
program.window.mainloop()