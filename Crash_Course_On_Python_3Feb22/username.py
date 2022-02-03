def hint_username(username):
    if len(username)<3:
        print("Invalid Username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid Username. Must be at most 15 characters long")
    else:
        print("Valid username!!!.")
username=input("Enter Username: ")

hint_username(username)