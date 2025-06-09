# code for budgeting program

import tkinter as tk # GUI
from tkinter import ttk
from dataHistory import save_user_info, load_user_info, save_monthly_data, load_monthly_data

class GUI:

    # initializing frame
    def __init__(self):

        # window for the entire program
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window.title("Smart Budgeter")
        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)

        # list for all the frames
        self.frames = {}

        # loops through all the frames and stores it in the list
        for f in (NameFrame, GoalFrame, MenuFrame, BudgetFrame, HistoryFrame, RecFrame):
            frame = f(self.window, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        # loads existing user info (name, goal) if applicable
        self.userData = load_user_info()

        # begins with the name frame if the user is new, otherwise it goes to the main menu
        if self.userData and "name" in self.userData and "goal" in self.userData:
            # Set goal reminder if goal exists
            self.frames[BudgetFrame].goalReminder.config(text = f"Goal: {self.userData['goal']}")
            # Set welcome label in GoalFrame just in case
            self.frames[GoalFrame].welcomeLabel.config(text = f"Welcome, {self.userData['name']}!")
            # Sends to menu
            self.show_frame(MenuFrame)
        else:
            self.show_frame(NameFrame)

    # switches between frames
    def show_frame(self, frame):

        self.frames[frame].tkraise()

    # personalizes experience, keeps name
    def personalize(self):

        name_frame = self.frames[NameFrame]
        name = name_frame.nameEntry.get().strip()

        if name:
            self.userData = load_user_info() or {}
            self.userData["name"] = name
            self.frames[GoalFrame].welcomeLabel.config(text = f"Welcome, {name}!")
            self.show_frame(GoalFrame)

    # puts goal on the screen as a reminder
    def goal_reminder(self):

        goal_frame = self.frames[GoalFrame]
        goal = goal_frame.goalEntry.get().strip()

        if self.userData is None:
            self.userData = {}

        self.userData["goal"] = goal
        save_user_info(self.userData, goal)
        self.frames[BudgetFrame].goalReminder.config(text = f"Goal: {goal}")
        self.show_frame(MenuFrame)

    # links the data to the month and stores it
    def submit_month(self):

        month_frame = self.frames[BudgetFrame]
        month = month_frame.monthEntry.get().strip()

        if not month:
            return

        # list for all the data for that month
        data = {
            "income": float(month_frame.incomeEntry.get()),
            "food": float(month_frame.foodEntry.get()),
            "utilities": float(month_frame.utilEntry.get()),
            "transport": float(month_frame.transportEntry.get()),
            "personal": float(month_frame.personalEntry.get()),
            "savings": float(month_frame.savingsEntry.get())
            }

        save_monthly_data(month, data)  # saves it before it gets deleted
        month_frame.monthEntry.delete(0, 'end')  # removes the data so new data can be entered
        month_frame.incomeEntry.delete(0, 'end')
        month_frame.foodEntry.delete(0, 'end')
        month_frame.utilEntry.delete(0, 'end')
        month_frame.transportEntry.delete(0, 'end')
        month_frame.personalEntry.delete(0, 'end')
        month_frame.savingsEntry.delete(0, 'end')

    # displays all the data neatly in the Budget History screen
    def display_history(self):

        history_frame = self.frames[HistoryFrame]
        history_frame.historyText.delete("1.0", tk.END) # prevents old data from overlapping
        data = load_monthly_data()

        # no history
        if not data:
            history_frame.historyText.insert(tk.END, "No budgeting data found.\n")

        else:
            for month, details in data.items():
                history_frame.historyText.insert(tk.END, f"{month}:\n")
                for key, value in details.items():
                    history_frame.historyText.insert(tk.END, f"  {key}: ${value}\n")
                history_frame.historyText.insert(tk.END, "\n")

        self.show_frame(HistoryFrame)

# frame where user enters name
class NameFrame(tk.Frame):

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)

        # title of frame
        ttk.Label(master = self, text = "Smart Budgeter", font = ("Times New Roman", 30)).pack(padx = 210, pady = 30)
        # asks user to enter name, stores it in a variable
        ttk.Label(master = self, text = "Enter your name", font = ("Times New Roman", 14)).pack(pady = 10)
        # name box
        self.nameEntry = ttk.Entry(master = self, font = ("Times New Roman", 10), width = 30)
        self.nameEntry.pack(pady = 10)
        # button to go next
        ttk.Button(master = self, text = "Enter", command = controller.personalize).pack(pady = 5)

# frame where user enters goal, personalization
class GoalFrame(tk.Frame):

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)

        # title of frame
        self.welcomeLabel = ttk.Label(master = self, text = "", font = ("Times New Roman", 30))
        self.welcomeLabel.pack(pady = 20)
        # question about goal, stores goal into variable
        ttk.Label(master = self, text = "What is your budgeting goal?", font = ("Times New Roman", 14)).pack(pady = 5)
        # entry box for the goal
        self.goalEntry = ttk.Entry(master = self, font = ("Times New Roman", 10), width = 50)
        self.goalEntry.pack(pady = 20)
        # button to go next to budgeting function
        ttk.Button(master = self, text = "Enter", command = controller.goal_reminder).pack(pady = 15)

# frame where user can navigate to other frames
class MenuFrame(tk.Frame):

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)

        # title of menu
        ttk.Label(master = self, text = "Main Menu", font = ("Times New Roman", 24)).pack(pady = 20)
        # budgeting tool
        ttk.Button(master = self, text = "Monthly Budget", command = lambda: controller.show_frame(BudgetFrame)).pack(pady = 10)
        # budgeting history
        ttk.Button(master = self, text = "Budget History", command = controller.display_history).pack(pady = 10)
        # recommendations
        ttk.Button(master = self, text = "Recommendations", command = lambda: controller.show_frame(RecFrame)).pack(pady = 10)

# frame where user budgets at a monthly rate
class BudgetFrame(tk.Frame):

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)

        # puts goal on top for reminder
        self.goalReminder = ttk.Label(master = self, text = "", font = ("Times New Roman", 14))
        self.goalReminder.pack(pady = 10)
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
        self.foodEntry.pack(pady = 5)
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

# frame where user can view their budgeting history if applicable
class HistoryFrame(tk.Frame):

    def __init__(self, master, controller):

        tk.Frame.__init__(self, master)

        self.historyText = tk.Text(master = self, height = 20, width = 80)
        self.historyText.pack(pady = 10)
        ttk.Button(master = self, text = "Back to Main Menu", command = lambda: controller.show_frame(MenuFrame)).pack(pady = 10)

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