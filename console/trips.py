# imports within python.
import pandas as pd
from datetime import date

# ------------------------------------------------------------
# imports from my the directory itself.
from trips_sql import View_trips, View_costs, View_contribution, Add_contribution
from db import query_db


# ------------------------------------------------------------
# >> (INDIVIDUAL) TRIP FUNCTION <<
# This serves as the placeholder for the welcome page.
# This is the function that is run on the main.py.
# The user arrives at this page after a successful log in in dashboard sends them back to main, and this function is triggered.
# ------------------------------------------------------------



# ------------------------------------------------------------
# START OF CORE FUNCTION
def trip():
    # Retrieve 'session' user
    session_user_file = open('session_user.txt','r')  # retreiving the session user id which is common across all the tan;
    member_id = session_user_file.read()
    session_user_file.close()

    # Retrieve 'session' trip
    session_trip_file = open('session_trip.txt','r')  # retreiving the session user id which is common across all the tan;
    trip_id = session_trip_file.read()
    session_trip_file.close()
    # Querying db for total costs and contribution
    # These variables are fixed so it they don't need to be repeated in recursive functions.
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

    # Using the member_id and trip_id to pull all the Trip table variables. These will be needed in the code.
    contribution = View_contribution(trip_id,member_id)
    total_contribution = contribution.view_contribution()
    total_contribution = total_contribution[0][0]

    costs = View_costs(trip_id)
    total_costs = costs.view_total_cost()
    total_costs = total_costs[0][0]

    # Calculate contributions
    remaining_contribution = total_costs - total_contribution

    # Getting costs per person
    individual_cost = total_costs / group_size

    # Getting the start date countdown.
    current_date = date.today()
    countdown = (start_date - current_date).days

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"🤔 Let's explore {trip_name}.\n")
    print(f"You leave for your holiday in {countdown} days!\n")
    print(f"The total group costs for your trip come to: {total_costs}")
    print(f"This comes to {individual_cost} per person.")
    print(f"You have {remaining_contribution} left to pay.")

    # Giving user the chance to add a contribution.
    prompt_add_contribtion()


# # ------------------------------------------------------------

# Here we planned to have a breakdown of costs, including using matplotlib for a pie chart.
# # Costs overview functions
# def prompt_costs_overview():
#     print("cost overview prompt placeholder")
#     prompt_add_contribtion()


# ------------------------------------------------------------
# Contribution functions
def prompt_add_contribtion():
    while True:
        prompt_add_contribution = input(
            "\n> Would you like to let us know about a new contribution? ('Y' or 'N'): ").upper()
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
    print(f"\nGreat!")

    while True:
        try:
            # Retrieve 'session' user
            session_user_file = open('session_user.txt','r')  # retreiving the session user id which is common across all the tan;
            member_id = session_user_file.read()
            session_user_file.close()

            # Retrieve 'session' trip
            session_trip_file = open('session_trip.txt','r')  # retreiving the session user id which is common across all the tan;
            trip_id = session_trip_file.read()
            session_trip_file.close()

            # fetch variables again in new function.
            contribution = View_contribution(trip_id, member_id)
            total_contribution = contribution.view_contribution()
            total_contribution = total_contribution[0][0]
            # Getting user input and converting it to integer
            input_contribution = input("Please enter the amount you would like to add: ").strip()
            input_contribution = int(input_contribution)  # Convert input to integer

            # Checking if the new contribution is valid (non-negative)
            if input_contribution < 0:
                raise ValueError

            # Update the data in SQL.
            new_total = input_contribution + total_contribution
            update_contribution = Add_contribution(new_total, member_id, trip_id)
            update_contribution.update_contribution()

            print(f"\n🎉 {input_contribution} was successfully added to your contribution total!")

            break  # Exit the loop if contribution addition is successful

        except ValueError:
            print(
                f"\n⚠️ Error: Contribution must be entered only as an integer (e.g., '200'). Please enter 0 if there is no new contribution.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    trip()


# ------------------------------------------------------------
# Ending trip 'session' and returning to user dashboard.
def exit_trip():
    from dashboard import dashboard

    while True:
        exit_trip = input("> Would you like to exit this trip view? ('Y' or 'N'): ").upper()

        if exit_trip == 'Y' or exit_trip == 'YES':
            print("\nThank you for logging in. See you next time! ✈️")
            dashboard()
            break

        elif exit_trip == 'N' or exit_trip == 'NO':
            trip() # Call the top of this 'webpage' again so user can view deshboard, add trip, or select to go to trips page.
            break

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")