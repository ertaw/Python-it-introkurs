users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def menu(title, prompt, options):
    print(f"{title}\n")
    for i in options:
        print(f"{i}) {options[i]}")
    while 1 == 1:
        inp = input(f"\n{prompt}")  
        if inp in options:
            print()
            return inp

def login(users):
    options = {"r":"Try again", "q":"Quit"}
    while 1==1:
       user = input("\nUser:")
       password = input("Password:")
       if user in users and password in users[user]:
           print("\nWelcome", user)
           return user
       else:
           if menu("", "Option:", options) == "q":
               break
               
login(users)