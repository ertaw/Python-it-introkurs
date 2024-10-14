
options = {"a":"Add item", "l":"List items", "q":"Log out"}

def menu():
    print("Select an action\n")
    for i in options:
        print(f"{i}) {options[i]}")
    while 1 == 1:
        inp = input("\nOption:")  
        if inp in options:
            print(f"\nYou seleted option {inp}) {options[inp]}") 
            break
      
    
menu()