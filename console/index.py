from logins_sql import Authentication

# ------------------------------------------------------------
# >> WELCOME FUNCTION <<
# This serves as the placeholder for the welcome page.
# This is the function that is run on the main.py.
# ------------------------------------------------------------

def welcome():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("""
    \n👋 Welcome to BudgetBuddy \n
    We're an innovative travel and budgeting console to help travellers plan their trips more efficiently and economically.
    Our travel and budgeting website provides a comprehensive range of tools and features 
    to streamline the vacation planning and budgeting process. 
    Members have easy access to total contributions, which alleviates some of the stress of holiday planning as a group. \n
    """)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("> Please tell us whether you want to login, or create an account.\n")
    print("For 'login', enter: L\n"
          "For 'create an account', enter: C\n")

    handling_login() # This brings the console to the login handling in the next function.

# ------------------------------------------------------------
# Function to create error handling loop for log in input choice option.
def handling_login():

        while True:

            login_choice = input("Please provide corresponding letter only here ('L' or 'C'): ").upper() # making sure it can make if statements

            if login_choice == 'L':
                login() # Sends console to login function bellow.
                break

            elif login_choice == 'C':
                create_account() # Sends console to create_account function bellow.
                break

            else:
                # Input error handling using while loop, error doesn't break console running.
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n⚠️ Oh no! I don't recognise your answer.")
                print("Please only enter the letter 'L' or 'C' to proceed.")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ------------------------------------------------------------
# Login function to authenticate user.
# This uses functions from the Authentication Class in the logins file.
def login():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n ✨ Welcome back! ")
    print("\n Please enter your username, then your password. \n")

    username = input("Username: ")
    password = input("Password: ")

    # passing variables to Authentication class.
    authenticate = Authentication(username, password)
    # Checking if the user exists
    if authenticate.check_user_exists():
        print("Username success.")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n⚠️ Username does not exist.")

    # Checking if the password matches
    if authenticate.check_password_match(): # this function returns a boolean value.
        member_id = authenticate.retrieve_member_id()
        session_user_file = open('session_user.txt','w')  # w replaces text so it means the session user is resubmitted every time the function logs in.
        session_user_file.write(f'{member_id}')  # store the member_id so the dashboard has an easy reference to call.
        session_user_file.close()

        # code will finish running this python file here, return to main, and run the dashboard python file.
    else:
        print("⚠️ Incorrect details provided.")
        retry_login() # function which handles the login error.

# ------------------------------------------------------------
# Error handling the login error.
# The function from the Authentication class is designed to return a boolean value which enables easy handling.
def retry_login():

    while True:

        retry_login = input("Would you like to to try again? ('Y' or 'N'): ").upper()
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        if retry_login == 'Y' or retry_login == 'YES':
            login() # recursively call back the function to loop the input prompt again.
            break

        elif retry_login == 'N' or retry_login == 'NO':
            print("\n No problem, we'll take you back to the homepage.")
            welcome()
            break

        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n⚠️ Oh no! I don't recognise your answer.")
            print("Please only enter the letter 'Y' or 'N' to proceed.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ------------------------------------------------------------
# Back-end workaround, storing member_id to file to have retrievable session reference (would use sessions from flask in webapp to do this)



# ------------------------------------------------------------
def create_account():
    print("Create account code placeholder")