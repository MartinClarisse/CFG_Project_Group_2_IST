
from db import query_db
from trips_sql import Retrieve_trip_id
from datetime import datetime
from trips_sql import Enter_trip
from dashboard import dashboard


def create_trip():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n🏖️ Amazing!")
    print("\n We just need to get some details about the trip to add it to your account.\n")
    insert_trip_table()





def insert_trip_table():

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
            start_date = input("Please enter the start (YYYY-MM-DD): ").strip()
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
            #
            # print("Error: Group size must be an integer (e.g., '6'). Please try again.")

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
            print(f"\n⚠️ Error: Costs must be entered as integers only (e.g., '200'). Please enter 0 if there is no cost.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    dashboard()





 #
 #
 #    new_trip =
 #
 # user = User(member_name, member_email, username, password)
 #
 #            if user.check_unique_email():
 #                raise ValueError(
 #                    "The email address you entered is already in use. Please try again with a different email address.")
 #
 #            if user.check_unique_username():
 #                raise ValueError(
 #                    "The username you entered is already in use. Please try again with a different username.")
 #
 #            user.insert_member_details()
 #            user.insert_authentication_details()




create_trip()

