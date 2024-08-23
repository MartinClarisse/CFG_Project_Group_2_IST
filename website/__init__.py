from flask import Flask

# ------------------------------------------------------------
# Creating the function which creates the web app.
# This imports the views from a views file.

def create_app():
    app = Flask(__name__)
    app.secret_key = "Example123" # needed for session encryption
    app.config['SECRET_KEY'] = 'Example123' # Adding for practise.

    from views import views
    app.register_blueprint(views)

    return app

