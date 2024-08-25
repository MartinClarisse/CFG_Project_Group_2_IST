# imports within python.
import pandas as pd
from datetime import date

# ------------------------------------------------------------
# imports from my the directory itself.
from trips_sql import View_trips, View_costs, View_contributions
from db import query_db
from dashboard import dashboard

# ------------------------------------------------------------
# >> (INDIVIDUAL) TRIP FUNCTION <<
# This serves as the placeholder for the welcome page.
# This is the function that is run on the main.py.
# The user arrives at this page after a successful log in in dashboard sends them back to main, and this function is triggered.
# ------------------------------------------------------------

# Beginning will pulling all the variables from SQL that are needed.
# Core function begins immediately below.

# Retrieve 'session' user
session_user_file = open('session_user.txt','r')  # retreiving the session user id which is common across all the tan;
member_id = session_user_file.read()
session_user_file.close()

# Retrieve 'session' trip
session_trip_file = open('session_user.txt','r')  # retreiving the session user id which is common across all the tan;
trip_id = session_trip_file.read()
session_trip_file.close()

# Using the member_id and trip_id to pull all the Trip table variables. These will be needed in the code.

query = "SELECT trip_name FROM Trips WHERE member_id = %s and trip_id = %s;"
args = (member_id, trip_id)
result = query_db(query, args)
trip_name = result[0][0]

query = "SELECT start_date FROM Trips WHERE member_id = %s and trip_id = %s;"
args = (member_id, trip_id)
result = query_db(query, args)
start_date = result[0][0]

query = "SELECT group_size FROM Trips WHERE member_id = %s and trip_id = %s;"
args = (member_id, trip_id)
result = query_db(query, args)
group_size = result[0][0]

# Getting the start date countdown.
current_date = date.today()
countdown = (start_date - current_date).days

# Querying db for total costs and contributions
costs = View_costs(trip_id)
total_costs = costs.view_total_cost()
total_costs = total_costs[0][0]

contributions = View_contributions(member_id, trip_id)
total_contributions = contributions.view_contribution()
total_contributions = total_contributions[0][0]

# Solving the remaining contributions.
remaining_contributions = total_costs - total_contributions

# ------------------------------------------------------------
# START OF CORE FUNCTION
def trip():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"🤔 Let's explore {trip_name}.\n")
    print(f"You leave for your holiday in {countdown} days!\n")
    print(f"The total group costs for your trip come to: {total_costs}")
    print(f"You have {remaining_contributions} left to pay.")
    prompt_costs_overview()

# ------------------------------------------------------------
# Costs overview functions
def prompt_costs_overview():
   print("cost overview prompt placeholder")
   prompt_add_contribtion()

# ------------------------------------------------------------
# Contributions functions
def prompt_add_contribtion():
    while True:
        prompt_add_contribution = input("\n> Would you like to let us know about a new contribution? ('Y' or 'N'): ").upper()
        if prompt_add_contribution == 'Y' or prompt_add_contribution == 'YES':
            add_contribution()
            break

        elif prompt_add_contribution == 'N' or prompt_add_contribution == 'NO':
            # Asking user if they want to add a new trip instead.
            exit_trip()
            break

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")



def add_contribution():
    print("add contribution placeholder")


# ------------------------------------------------------------
# Ending trip 'session' and returning to user dashboard.

def exit_trip():
    print("this is a placehoder to exit trip page")


trip()