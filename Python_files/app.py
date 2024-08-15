import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9731",
)

print(mydb)
