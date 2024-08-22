import mysql.connector

# ------------------------------------------------------------

# This file has functions for connecting to the database, then querying and closing it.
# This means the functions can be called in the models file without needing to be repeated each time.
# For example, you would just import * functions then just define the query and pass it through the query_db function.

# ------------------------------------------------------------
# This function connects to the database
# ❗NB: The password needs to be changed for programmer's own MySQL log in to connect.

def get_db():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9731",
    database="BudgetBuddy"
    )

# ------------------------------------------------------------
# This function allows you to query the database by passing in the query (SELECTS AND INSERTS ETC).
def query_db(query, args=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    db.close()
    return rv

# ------------------------------------------------------------
# Quick check it works... (it does hooray!, This can be properly tested in the testing file once everything working)
# query = "SELECT * FROM Trips"
# results = query_db(query)
# print(results)

