#recommendation window

import tkinter as tk
from tkinter import ttk

def recommendations_frame(self):
    frame = self.frames["recommendationsFrame"]
    recommendations = """
    Recommended Budgeting Rule (50/30/20):

    - 50% Needs: rent, bills, groceries, transportation, etc.
    - 30% Wants: entertainment, hobbies, shopping, etc.
    - 20% Savings: savings account, investment, emergency fund
    """
    ttk.Label(master = frame, text = 'Recommendations', font = ('Arial', 18)).pack(pady = 10)
    tk.Label(master = frame, text = recommendations, font = ('Arial', 14), justify = "left").pack(padx = 20)
    ttk.Button(master = frame, text = 'Back to Main Menu', command = lambda: self.new_frame("menuFrame")).pack(pady = 10)