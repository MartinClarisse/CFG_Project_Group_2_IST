from logins_sql import User

def create_account():
    print("Create account code placeholder")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n ✨ Welcome New User! ")
    print("\n We just need to get some of your information and then we can create your account.\n")

    while True:
        try:
            # Getting and validating member name
            member_name = input("Please enter your name: ").strip()
            if not member_name:
                raise ValueError("Name cannot be empty.")

            # Getting and validating member email
            member_email = input("Please enter your email address: ").strip()
            if not member_email:
                raise ValueError("Email cannot be empty.")

            # You would also need to get the username and password from the user
            username = input("Please enter a username: ").strip()
            if not username:
                raise ValueError("Username cannot be empty.")

            password = input("Please enter a password: ").strip()
            if not password:
                raise ValueError("Password cannot be empty.")

            # Check if the email already exists in the database
            check_user = User(member_name, member_email, username, password)

            if check_user.check_unique_email():
                raise ValueError(
                    "The email address you entered is already in use. Please try again with a different email address.")

            if check_user.check_unique_username():
                raise ValueError(
                    "The username you entered is already in use. Please try again with a different username.")


            print("\n🎉 Account created successfully!")
            break  # Exit the loop if account creation is successful

        except ValueError as ve:
            print(f"\n⚠️ Error: {ve}")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except Exception as e:
            print(f"\n⚠️ Unexpected error: {e}")
            print("Please try again.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

create_account()