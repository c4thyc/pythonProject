# user budgeting and spending history (monthly)

import json # for storing the data and budget history
import os # saves data

# files to store user data, automatically created with the name after use enters their budgeting information
userData = "userData.json"  # name, goal
budgetData = "budgetData.json" # budgeting info per month

# saves the start screen info (name and goal)
def save_user_info(userData, goal):

    userData["goal"] = goal
    with open("userData.json", "w") as file:
        json.dump(userData, file) # stores goal data in JSON file

# loads name and goal (if applicable) when user runs program again
def load_user_info():

    if os.path.exists("userData.json"):
        with open("userData.json", "r") as file:
            return json.load(file) # returns data if any
    return None

# saves the data for each month in JSON file
def save_monthly_data(month, budgetInfo):

    filename = "budgetData.json"
    if os.path.exists(filename): # checks if there's already budgeting data
        with open(filename, "r") as file:
            existing_data = json.load(file) # loads the existing budgeting data
    else:
        existing_data = {} # makes a new list if none
    existing_data[month] = budgetInfo # stores the new info in list
    with open(filename, "w") as file:
        json.dump(existing_data, file) # stores info from list into JSON file

# loads monthly budgeting data
def load_monthly_data():

    filename = "budgetData.json"
    if os.path.exists(filename): # checks if there is already budgeting data stored
        with open(filename, "r") as file:
            return json.load(file) # returns the data from JSON file
    return {}