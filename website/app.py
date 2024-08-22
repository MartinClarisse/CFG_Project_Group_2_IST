from website.__init__ import create_app

# ------------------------------------------------------------

# Here is where the webapp is actually launched from and runs from.
# The app is called from the imported create_app function.

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000) #debug reruns script with changes and helps to indentify issues.






