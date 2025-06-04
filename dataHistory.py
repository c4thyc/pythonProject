#user budgeting and spending history (monthly)

import json #for storing the data and budget history
import os

#files to store user data, automatically created with the name after use enters their budgeting information
userData = "userData.json"  #name, goal
budgetData = "budgetData.json" #budgeting per month

#functions for saving user data history---------

#saves the start screen info (name and goal)
def save_user_info(userData, goal):
    userData["goal"] = goal
    with open("userData.json", "w") as f:
        json.dump(userData, f)

#loads the history when user runs program again
def load_user_info():
    if os.path.exists("userData.json"):
        with open("userData.json", "r") as f:
            return json.load(f)
    return None

#budgeting data-------

#saves the data for each month
def save_monthly_data(month, budgetInfo):
    filename = "budgetData.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = {}

    existing_data[month] = budgetInfo
    with open(filename, "w") as f:
        json.dump(existing_data, f)

def load_monthly_data(month):
    filename = "budgetData.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}