# imports within python.
import pandas as pd
from datetime import datetime

# ------------------------------------------------------------
# imports from my the directory itself.
from trips_sql import View_trips, Retrieve_trip_id, Enter_trip
from db import query_db
from index import index

# ------------------------------------------------------------
# >> DASHBOARD FUNCTION <<
# This serves as the placeholder for the welcome page.
# This is the function that is run on the main.py.
# The user arrives at this page after a successful log in in dashboard sends them back to main, and this function is triggered.
# ------------------------------------------------------------
def dashboard():

    # Retrieving the 'session' member_id from the file to pass to SQL to load session dashboard.
    session_user_file = open('session_user.txt','r') #retreiving the session user id which is common across all the tan;
    member_id = session_user_file.read()
    session_user_file.close()

    # Retrieving member_name with user_id for a personal touch.
    query = "SELECT member_name FROM Member_details WHERE member_id = %s;"
    args = (member_id,)
    result = query_db(query, args)
    member_name = result[0][0]

    # Intro message to dashboard
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"Hi {member_name}, welcome to your dashboard.\n")

    # Retrieving trip list
    view_trips = View_trips(member_id)
    trips = view_trips.view_trip()

    if trips:
        print("🌴 Here are your trips:\n")
        df_trips = pd.DataFrame(trips, columns=['Trip Name'])  # Converting it from list of tuples, changing column name to Trip Name.
        df_trips.index += 1  # Fixing index to start at 1
        print(df_trips)

        # Asking user if they want to move on to trips page
        prompt_trips_page()


    else:
        print("😔 You haven't currently got any trips registered yet....\n")
        # ASking user if they want to add a new trip.
        prompt_new_trip()

    # End of core function, the code will have moved on to the following 'routes' below.

# ------------------------------------------------------------
# Letting the user select a trip.
def prompt_trips_page():
    # while loop to handle incorrect inputs.
    while True:
        prompt_trips_page = input("\n> Would you like to explore one of these trips? ('Y' or 'N'): ").upper()
        if prompt_trips_page == 'Y' or prompt_trips_page == 'YES':
            select_trip()
            break

        elif prompt_trips_page == 'N' or prompt_trips_page == 'NO':
            # Asking user if they want to add a new trip instead.
            prompt_new_trip()
            break

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# ------------------------------------------------------------
# Function which asks user if they want to add a new trip
def prompt_new_trip():
    # while loop to handle incorrect inputs.
    while True:

        prompt_trip = input("> Would you like to tell us about a new trip? ('Y' or 'N'): ").upper()

        if prompt_trip == 'Y' or prompt_trip == 'YES':
            new_trip()  # Calls function below which deals with gathering variables to insert into trips/costs/contribution table.
            break

        elif prompt_trip == 'N' or prompt_trip == 'NO':
            logout()  # Function which gives user a chance to restart the console.
            break

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# ------------------------------------------------------------
# Function which takes in input variables from user to insert into SQL database.
def new_trip():

    # Pulling user_id again, needed for the table.
    session_user_file = open('session_user.txt','r')  # retreiving the session user id which is common across all the tan;
    member_id = session_user_file.read()
    session_user_file.close()


    while True:
        try:
            # Getting and validating trip name
            trip_name = input("Please enter the trip name: ").strip()
            if not trip_name:
                raise ValueError("Trip name cannot be empty.")
            break

        except ValueError as ve:
            print(f"\n⚠️ Error: {ve}")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        try:
            # Getting and validating start date
            start_date = input("Please enter the start (YYYY-MM-DD): ").strip() # to improve, should check to see if date is in the future.
            if not start_date:
                raise ValueError("Start date cannot be empty.")

            check_date = datetime.strptime(start_date, '%Y-%m-%d')
            break

        except ValueError:
            # Telling user the date format is wrong.
            print("Error: The date must be in the format YYYY-MM-DD (e.g., '2024-08-24'). Please try again.")

    while True:
        try:
            # Getting and validating group size
            group_size = input("Please enter the group size (must be an integer): ").strip()
            group_size = int(group_size)  # Convert input to integer

            if not group_size:
                raise ValueError("Group size cannot be empty.")

            break

        except ValueError:
            print(f"\n⚠️ Error: {ve}")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # The costs can all be error handled in the same block thankfully.
    while True:
        try:
            flights_total = input("\nPlease enter the total cost of the flights: ").strip()
            flights_total = int(flights_total)
            if not group_size:
                raise ValueError()

            accomodation_total = input("Please enter the total cost of the accomadation: ").strip()
            accomodation_total = int(accomodation_total)
            if not group_size:
                raise ValueError()

            transfers_total = input("Please enter the total cost of the transfers: ").strip()
            transfers_total = int(transfers_total)
            if not group_size:
                raise ValueError()

            activities_total = input("Please enter the total cost of the activities: ").strip()
            activities_total = int(activities_total)
            if not group_size:
                raise ValueError()

            miscellaneous_total = input("Please enter any miscellaneous costs: ").strip()
            miscellaneous_total = int(miscellaneous_total)
            if not group_size:
                raise ValueError()

            # Passing variables to SQL databases.

            trip = Enter_trip(trip_name,start_date,group_size,member_id,flights_total,accomodation_total,transfers_total,activities_total,miscellaneous_total)
            trip.create_trip()
            trip.add_costs()
            trip.create_contributions() # creates the table defaulted at zero.

            print(f"\n🎉 {trip_name} was successfully added to your account!")

            break

        except ValueError:
            print(f"\n⚠️ Error: Costs must be entered only as integers (e.g., '200'). Please enter 0 if there is no cost.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Brings user back to their dashboard/homepage. They will be able to see their new trip added to their trip list when it brings them back.
    dashboard()


def select_trip():

    while True:
        trip_name = input("\n☀️ Great! Please enter the name of the trip you would like to view: ")

        # Query to check if trip name exists.
        query = "SELECT * FROM Trips WHERE trip_name = %s"  # To improve would also need to add user_id variable in query with AND, short of time sadly.
        args = (trip_name,)
        trip_exist = query_db(query, args)

        if trip_exist:
            # Fetching the trip_id from SQL.
            trips = Retrieve_trip_id(trip_name)
            trip_id = trips.retrieve_trip_id()
            # Back-end workaround, storing trip_id to file to have retrievable session reference for trips (would use sessions from flask in webapp to do this)
            session_trip_file = open('session_trip.txt', 'w')  # w replaces text so it means the session user is resubmitted every time the function logs in.
            session_trip_file.write(f'{trip_id}')  # stores the trip_id so the dashboard has an easy reference to call.
            session_trip_file.close()

            break
            # This break ends the code on this file, so the console is redirected to main which now calls third and final function trips.

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise that trip name.")
            print("Please type in the trip name exactly as it is written. Note that this input is case sensitive.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# ------------------------------------------------------------
# Prompts user to 'logout' which ends their 'session' and returns them to the dashboard/ restarts console app logic...
def logout():
    # prompt user to logout. Same logic for while loop to handle input errors.
    while True:

        logout = input("> Would you like to log out of your account? ('Y' or 'N'): ").upper()

        if logout == 'Y' or logout == 'YES':
            print("\nThank you for logging in. See you next time! ✈️")
            # End 'session' for user by deleting their member_id from session file.
            # This is just for good practice as each time the login functions runs the 'w' functions overrides the member_id anyway.
            session_user_file = open('session_user.txt','w')  # retreiving the session user id
            session_user_file.truncate()
            session_user_file.close()
            # Finally, send user back to the first function from the index. This is to serve back as an almost hyperlink.
            index()
            break

        elif logout == 'N' or logout == 'NO':
            dashboard() # Call the top of this 'webpage' again so user can view deshboard, add trip, or select to go to trips page.
            break

        else:
            # Input error handling using while loop, error doesn't break console running.
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


