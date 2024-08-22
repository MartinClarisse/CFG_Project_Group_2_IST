from db import get_db, query_db
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
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def check_user_exists(self):
        query = "SELECT * FROM  Authentication WHERE username = %s" # Used args instead of f string to avoid SQL injection attacks
        args = (self.username,)
        results = query_db(query, args)
        return bool(results) # better than if clause for True or False

    def check_password_match(self):
        hashed_password = hashlib.md5(self.password.encode()).hexdigest() # This matches the encryption which happens when a user is created with the query.
        query = "SELECT * FROM  Authentication WHERE username = %s AND PWD = %s"
        args = (self.username, hashed_password,)
        results = query_db(query, args)
        return bool(results)



# 'Testing' the Class to make sure authentication works properly'
# Rather than this, this would need to then use the boolean values in if statements on view to determine wether to move on to dashboard or raise error.

# Using our Dud
username = 'thedud'
password = 'password'

authenticate = Authentication(username, password)



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

