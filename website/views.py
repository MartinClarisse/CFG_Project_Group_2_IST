from flask import Blueprint, render_template, request
views = Blueprint(__name__,'views')

@views.route("/")
def home():
    return render_template("index.html", methods=["GET", "POST"])

@views.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@views.route("/trips", methods=["GET", "POST"])
def trips():
    return render_template("trip.html")

# @views.route("/json")
# def get_json():
#     return jsonify()