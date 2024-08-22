from db import query_db, insert_db
import hashlib # Needed for authentication
# ------------------------------------------------------------

# This is a file which puts all the code which queries SQL.
# So once the variables are taken from the inputs in the views, they can be passed into functions here and returned to views.
# I'm thinking this will probably end up wth more files, like one for each page I imagine?
# And to save on replicating code, the actual db function gets called from db so only a query needs to be passed.
# Here I am unsure if it needs classes or can just be functions?


# ------------------------------------------------------------
# How to authenticate the user login inputs from html
class Authentication:

    # Initnitialising class with the values for the Authentication table.
    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password

    def check_user_exists(self):
        query = "SELECT * FROM  Authentication WHERE username = %s;" # Used args instead of f string to avoid SQL injection attacks
        args = (self.user_name,)
        results = query_db(query, args)
        return bool(results) # better than if clause for True or False

    def check_password_match(self):
        hashed_password = hashlib.md5(self.password.encode()).hexdigest() # This matches the encryption which happens when a user is created with the query.
        query = "SELECT * FROM  Authentication WHERE username = %s AND PWD = %s;"
        args = (self.user_name, hashed_password,)
        results = query_db(query, args)
        return bool(results)



# 'Testing' the Class to make sure authentication works properly'
# Rather than this, this would need to then use the boolean values in if statements on view to determine wether to move on to dashboard or raise error.

# Using our Dud
user_name = 'thedud'
password = 'password'

authenticate = Authentication(user_name, password)



# Checking if the user exists
if authenticate.check_user_exists():
    print("User exists")
else:
    print("User does not exist")

# Checking if the password matches
if authenticate.check_password_match():
    print("Password matches")
else:
    print("Password does not match")

# ------------------------------------------------------------
# Sending new user variables into the SQL database.
class User:
    # Initnitialising class with the values for the Member_id and Authentication table.
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
    def insert_member_details(self):
        insert = "INSERT INTO Member_Details (member_name, email) VALUES (%s, %s);"
        args = (self.name, self.email)
        rows_affected = insert_db(insert, args)
        return rows_affected

    def insert_authentication_details(self):
        # Fetching the member_id as it's the FK
        query = "SELECT member_id FROM Member_details WHERE member_name = %s;"
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