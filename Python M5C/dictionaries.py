
#users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
#data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

#def dictionaries(users, data):
    #print("Användare:\n")
    #for i in users:
     #   print(f"{i}")
    #print("\nAnvändare och lösenord:\n")
    #for i in users:
    #    print(f"{i}) {users[i]}")
    #print("\nAnvändare och deras data:\n")
    #for i in data:
    #    print(f"{i}) {data[i]}")
    #inp = str(input("\nSlå upp användare:"))
    #if inp not in users:
    #    print(f"\nAnvändaren {inp} finns inte")
    #else:
    #    print(f"\nData lagrat för {inp}: {data[inp]}")

def dictionaries(users, data):
    print("Användare:\n")
    for i in users:
        print(f"{i}")
    print("\nAnvändare och lösenord:\n")
    for i in users:
        print(f"{i}) {users[i]}")
    print("\nAnvändare och deras data:\n")
    for i in data:
        print(f"{i}) {data[i]}")
    inp = str(input("\nSlå upp användare:"))
    if inp not in users:
        print(f"\nAnvändaren {inp} finns inte")
    else:
        print(f"\nData lagrat för {inp}: {data[inp]}")

#dictionaries()
    