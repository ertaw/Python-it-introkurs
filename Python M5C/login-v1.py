
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login():
    user = input("User:")
    password = input("Password:")
    if user in users:
        if password in users[user]:
            print("Welcome", user)
    else:
        print("Invalid username or password")
        
login()