from db import query_db, insert_db
import datetime

# ------------------------------------------------------------
class Enter_trip:
    # Initialising the class with all the values from Trips and Costs Tables.
    def __init__(self, trip_name, start_date, group_size, member_id, flights_total, accomodation_total, transfers_total,
                 activities_total, miscellaneous_total):
        self.trip_name = trip_name
        self.start_date = start_date
        self.group_size = group_size
        self.member_id = member_id
        self.flights_total = flights_total
        self.accomodation_total = accomodation_total
        self.transfers_total = transfers_total
        self.activities_total = activities_total
        self.miscellaneous_total = miscellaneous_total

    def create_trip(self):
        insert = "INSERT INTO Trips (trip_name, start_date, group_size, member_id) VALUES (%s, %s, %s, %s);"
        args = (self.trip_name, self.start_date, self.group_size, self.member_id,)
        rows_affected = insert_db(insert, args)
        return rows_affected

    def add_costs(self):
        # Fetching the trip_id as it's the FK
        query = "SELECT trip_id FROM Trips WHERE trip_name = %s;"
        args = (self.trip_name,)
        result = query_db(query, args)
        trip_id = result[0][0]
        # Inserting Costs
        insert = "INSERT INTO Costs (trip_id, flights_total, accomodation_total, transfers_total, activities_total, miscellaneous_total) VALUES (%s, %s, %s, %s, %s, %s);"
        args = (trip_id, self.flights_total, self.accomodation_total, self.transfers_total, self.activities_total,
                self.miscellaneous_total)
        rows_affected = insert_db(insert, args)
        return rows_affected

    def create_contributions(self):
        # Fetching the trip_id as it's the FK
        query = "SELECT trip_id FROM Trips WHERE trip_name = %s;"
        args = (self.trip_name,)
        result = query_db(query, args)
        trip_id = result[0][0]
        # Creating the table with default values, these can be amended later.
        insert = "INSERT INTO Contributions (trip_id, member_id) VALUES (%s, %s);"
        args = (trip_id, self.member_id,)
        rows_affected = insert_db(insert, args)
        return rows_affected
# 'Testing' the Class to make sure creating trips and adding costs work properly.
# Again, this can be moved to the testing file and put in a proper Test Class.

# trip_name = 'Bahamas'
# start_date = datetime.date(2024, 1, 1)
# group_size = 2
# member_id = 2
# flights_total = 500
# accomodation_total = 600
# transfers_total = 100
# activities_total = 300
# miscellaneous_total = 150
#
# trip1 = Enter_trip(trip_name, start_date, group_size, member_id, flights_total, accomodation_total, transfers_total,
#              activities_total, miscellaneous_total)
#
# trip1.create_trip()
# trip1.add_costs()
# trip1.create_contributions()


# query1 = "SELECT * FROM Trips;"
# results = query_db(query1)
# print(results)
#
# query2 = "SELECT * FROM Costs;"
# results = query_db(query2)
# print(results)
#
# query3 = "SELECT * FROM Contributions;"
# results = query_db(query3)
# print(results)

# ------------------------------------------------------------

class View_trips:
    # These are the only variables to be inputted into the queries, the rest of the values get pulled
    def __init__(self, member_id):
        self.member_id = member_id

    def view_trip(self):
        query = "SELECT trip_name FROM Trips WHERE member_id = %s;" # In future, should add that date is upcoming as additional filter.
        args = (self.member_id,)
        trips = query_db(query, args)
        return trips

    def view_total_cost(self):
        query = "SELECT %s, (flights_total + accomodation_total + transfers_total + miscellaneous_total) AS total_cost FROM Costs;"
        args = (mem)

# ------------------------------------------------------------
class Retrieve_trip_id:
    def __init__(self, trip_name):
        self.trip_name = trip_name
    def retrieve_trip_id(self):
        query = "SELECT trip_id FROM Trips WHERE trip_name = %s;"
        args = (self.trip_name,)
        result = query_db(query, args)
        trip_id = result[0][0]
        return trip_id

# 'Testing' the Class to make sure you can see all trip names from member_id being passed in.
# Again, this can be moved to the testing file and put in a proper Test Class.

# member_id = '2'
# member_trips1 = View_trips(member_id)
# trips = member_trips1.view_trip()
# print(f"all trips ={trips}")


# ------------------------------------------------------------


class View_costs:
    def __init__(self, trip_id):
        self.trip_id = trip_id
    def view_costs(self):
        query = "SELECT * FROM Costs WHERE trip_id = %s;"
        args = (self.trip_id,)
        costs = query_db(query, args)
        return costs
    def view_total_cost(self):
        query = "SELECT (flights_total + accomodation_total + transfers_total + miscellaneous_total) AS total_cost FROM Costs WHERE trip_id = %s";
        args = (self.trip_id,)
        total_cost = query_db(query,args)
        return total_cost




# 'Testing' the Class to make sure fetching trip info works.
# Again, this can be moved to the testing file and put in a proper Test Class.

# trip_id = '2'
# trip1 = View_costs(member_id)
# costs = trip1.view_costs()
# print(f"total costs row= {costs}")

# ------------------------------------------------------------

class Add_contributions:
    def __init__(self, total, trip_id, member_id):
        self.trip_id = trip_id
        self.member_id = member_id
        self.total = total

    def update_contribution(self):
        insert = "UPDATE Contributions SET total=%s WHERE member_id = %s AND trip_id = %s;"
        args = (self.total, self.member_id, self.trip_id,)
        rows_affected = insert_db(insert, args)
        return rows_affected

# ------------------------------------------------------------

class View_contributions:

    def __init__(self, trip_id, member_id):
        self.trip_id = trip_id
        self.member_id = member_id
    def view_contribution(self):
        query = "SELECT * FROM Contributions WHERE member_id = %s AND trip_id = %s;"
        args = (self.member_id, self.trip_id)
        contribution = query_db(query, args)
        return contribution


# 'Testing' the Class to make sure updating and fetching contributions work.
# Again, this can be moved to the testing file and put in a proper Test Class.

# total = '150'
# trip_id = '2'
# member_id ='2'
#
# contribution = Contributions(total, trip_id, member_id)
#
# update_contribution = contribution.update_contribution()
#
# view_contribution = contribution.view_contribution()
# print(f"total contributions row: {view_contribution}")



