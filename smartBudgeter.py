#brings all the functions together for the app

import tkinter as tk
from tkinter import ttk

class Budget:
    def __init__(self, income):
        self.income = income
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))

    def total_expenses(self):
        return sum([amount for _, amount in self.expenses])

    def remaining_balance(self):
        return self.income - self.total_expenses()

    def summary(self):
        return {
            'Income': self.income,
            'Expenses': self.expenses,
            'Total Expenses': self.total_expenses(),
            'Remaining': self.remaining_balance()
        }