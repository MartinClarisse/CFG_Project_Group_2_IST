from flask import Blueprint, render_template, request, redirect, url_for, session
# ------------------------------------------------------------
# This is where the routes for the webapp are defined.
# There are three basic ones which just render the HTML templates.
# I've kept these just as the three to show you the connection itself is working.

views = Blueprint(__name__, 'views')
@views.route("/")
def home():
        return render_template("index.html")

@views.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

@views.route("/trips/")
def trips():
    return render_template("trip.html")


# ------------------------------------------------------------

# The problem I am having is actually passing the variables across. I have tried so many things!
# I have a suspition there may be an issue with the submit in the HTML triggering the action with the template file.
# Because the route changes on the webapp and is not reacheable.
# I think we need to use a redirect and url for after doing a SQL query instead and signpost it from the python not HTML.
# If we do this we may be able to also use session which should help massively for storing login variables?
# What I've got below doesn't work or make sense, I thought I'd show you the sort of things I was trying.
# I'll send you a diagram to how I think it should all work, but please change it if you think that's not working.

# @views.route("/")
# def home():
    # if request.method == "POST":
    #     user = request.form['username']
    #     password = request.form['password']
    #     session["user"] = user
    #     return redirect(url_for("dashboard"))
    # else:
    #     return render_template("index.html")

# @views.route("/dashboard/")
# def dashboard():
    # if "user" in session:
    #     user = session["user"]
    # return render_template("dashboard.html")
    # else:
    # return redirect(url_for("views.login"))
# def login():
#     user_name = request.form["user_name"]
#     password = request.form["password"]
#     return render_template("dashboard.html", user_name, password)

