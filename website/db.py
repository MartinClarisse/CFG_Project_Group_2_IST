import mysql.connector
from flask import current_app, g #g is special object in flask that stores informatio that's being handled.
from flask import Flask
# ------------------------------------------------------------

# Test Example, connection working
# cursor = mydb.cursor()
# query = "INSERT INTO Trips (trip_name, start_date)  VALUES (%s,%s);"
# data = ("Test", "2024-08-21")
# cursor.execute(query, data)
# mydb.commit()
# cursor.close()
# mydb.close()

# ------------------------------------------------------------

def get_mydb():
    if 'my_db' not in g:
        mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="9731",
        database="BudgetBuddy"
    )
        return g.my_db

def close_my_db(e=None):
    my_db = g.pop('my_db', None)
    if my_db is not None:
        my_db.close()

def query_my_db(query, args=(), one=False):
    db = get_mydb()
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv




# ------------------------------------------------------------

# class Trips(db.Model)
#     id = db.Column(db.Integer, primary_key=True)

# --------------------------------