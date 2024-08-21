from website.__innit__ import create_app

# ------------------------------------------------------------

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000) #debug reruns script with changes and helps to indentify issues.


# app.register_blueprint(views, url_prefix="/")






