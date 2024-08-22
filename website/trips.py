class Trips:
    def __init__ (self, trip_id, trip_name, start_date, flights_total, accomodation_total, transfers_total, activities_total, miscellaneous_total):


    def check_user_exists(self):
        query = "SELECT * FROM  Authentication WHERE username = %s" # Used args instead of f string to avoid SQL injection attacks
        args = (self.user_name,)
        results = query_db(query, args)
        return bool(results) # better than if clause for True or False

    def check_password_match(self):
        hashed_password = hashlib.md5(self.password.encode()).hexdigest() # This matches the encryption which happens when a user is created with the query.
        query = "SELECT * FROM  Authentication WHERE username = %s AND PWD = %s"
        args = (self.user_name, hashed_password,)
        results = query_db(query, args)
        return bool(results)


class User:
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
    def insert_member_details(self):
        insert = "INSERT INTO Member_Details (member_name, email) VALUES (%s, %s)"
        args = (self.name, self.email)
        rows_affected = insert_db(insert, args)
        return rows_affected

    def insert_authentication_details(self):
        query = "SELECT member_id FROM Member_details WHERE member_name = %s"
        args = (self.name,)
        result = query_db(query, args)
        member_id = result[0][0]
        insert = "INSERT INTO Authentication (username, member_id, PWD)VALUES (%s,%s,md5(%s));"
        args = (self.username, member_id, self.password,)
        rows_affected = insert_db(insert, args)
        return rows_affected

# 'Testing' the Class to make sure authentication works properly'
# Rather than this, this would need to then use the boolean values in if statements on view to determine wether to move on to dashboard or raise error.


# name = 'Rachel Green'
# email = 'rachel.green@gmail.com'
# username = 'rachelg'
# password = 'centralperk'
#
# user1 = User(name, email, username,password)
# user1.insert_member_details()
# user1.insert_authentication_details()

query1 = "SELECT * FROM Member_details;"
results = query_db(query1)
print(results)

query2 = "SELECT * FROM Authentication;"
results = query_db(query2)
print(results)