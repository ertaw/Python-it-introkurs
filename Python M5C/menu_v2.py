
def menu(title, prompt, options):
    print(f"{title}\n")
    for i in options:
        print(f"{i}) {options[i]}")
    while 1 == 1:
        inp = input(f"\n{prompt}")  
        if inp in options:
            print()
            return inp


#options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
#opt1 = menu("Select an action", "Action: ", options1)
#print(f"You selected action {opt1}) {options1[opt1]}")
#print()

#options2 = {"r":"Try again", "q":"Quit"}
#opt2 = menu("What do you want to do?", "My choice: ", options2)
#print(f"You selected option {opt2}) {options2[opt2]}")