#user budgeting and spending history (monthly)

import json #for storing the data and budget history
import os

#files to store user data, automatically created with the name after use enters their budgeting information
userData = "userData.json"  #name, goal
budgetData = "budgetData.json" #budgeting per month

#functions for saving user data history---------

#saves the start screen info (name and goal)
def save_user_info(name, goal):
    data = {
        "name": name,
        "goal": goal
    }
    #stores the info into json file
    with open(userData, "w") as f:
        json.dump(data, f)

#loads the history when user runs program again
def load_user_info():
    if os.path.exists(userData):
        with open(userData, "r") as f:
            return json.load(f)
    return None

#budgeting data-------

#saves the data for each month
def save_monthly_data(month, budgetInfo):
    #loads existing data
    allData = {}
    if os.path.exists(budgetData):
        with open(budgetData, "r") as f:
            allData = json.load(f)

    #saves and updates the current month's data
    allData[month] = budgetInfo

    with open(budgetData, "w") as f:
        json.dump(allData, f)

def load_all_budget_data():
    if os.path.exists(budgetData):
        with open(budgetData, "r") as f:
            return json.load(f)
    return {}

def load_monthly_data(month):
    allData = load_all_budget_data()
    return allData.get(month, None)