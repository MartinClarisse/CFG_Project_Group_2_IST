from index import index
from dashboard import dashboard
from trips import trip

# ------------------------------------------------------------
# ❗IMPORTANT:
# RUN THIS FILE TO LAUNCH 'BUDGETBUDDY' CONSOLE APP.
# This code is a placeholder for a webapp using HTML and flask.
# Therefore, the main python file runs only 3 functions, as these correspond to the equivalent 3 webpages.
# The 3 functions  are connected to their corresponding modules (index, dashboard, trips) which run the console logic.
# These act as equivalents for the HTML templates.
# These modules import Classes from files designated only for interacting with mysql.connector.
# The python-SQL files also import from db to easily execute queries and inserts.
# The misc_functions file holds any miscellaneous repeatable code in the console app.
# ------------------------------------------------------------

# THE CORE FUNCTIONS
# These are the central function for each of the equivalent HTML templates - python file substitutes.
def run_console():
    index()
    dashboard()
    trip()


run_console()