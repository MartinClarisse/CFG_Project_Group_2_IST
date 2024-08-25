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


# ------------------------------------------------------------

class Add_contribution:
    def __init__(self, new_total, trip_id, member_id):
        self.new_total = new_total
        self.trip_id = trip_id
        self.member_id = member_id

    def update_contribution(self):
        insert = "UPDATE Contributions SET total=%s WHERE member_id = %s AND trip_id = %s;"
        args = (self.new_total, self.member_id, self.trip_id)
        rows_affected = insert_db(insert, args)
        return rows_affected

# ------------------------------------------------------------

class View_contribution:

    def __init__(self, trip_id, member_id):
        self.trip_id = trip_id
        self.member_id = member_id
    def view_contribution(self):
        query = "SELECT total FROM Contributions WHERE member_id = %s AND trip_id = %s;"
        args = (self.member_id, self.trip_id)
        contribution = query_db(query, args)
        return contribution
