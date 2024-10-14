from dictionaries import dictionaries
from add_v2 import add
from login_v3 import login, menu
from view_v2 import view



options2 = {"r":"Try again", "q":"Quit"}
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
options3 = {"l":"Log in", "q":"Quit"}
users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

def main():
    if menu("Welcome to Lagra (TM)", "Option: ", options3) == "l":
        user = login(users)
        if (user != "0"):
            view("\nThese are your items:", data[user])
            while (user!= "0"):           
                choice = menu("\nSelect an action: ", "Option: ", options1)
                if (choice == "a"):
                    add("Add an item:",data[user])
                elif (choice == "l"):
                    view("\nThese are your items:", data[user])
                elif (choice == "q"):
                    choice = menu("Welcome to Lagra (TM)", "Option: ", options3)
                    if choice == "l":
                        user = login(users)
                        if (user != "0"):
                            view("\nThese are your items:", data[user])
                    elif (choice == "q"):
                        break
                    

    
main()
