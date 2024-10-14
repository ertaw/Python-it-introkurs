
#names   = ["nisse", "stina", "bosse", "mimmi"]
#animals = ["giraff", "myrslok", "tapir"]

def view(description, strings):
    number = 1
    print(description)
    print()
    for i in strings:
        print(f"{number}) {i}")
        number += 1

#view("Lista med namn", names)
#print()
#view("Lista med djur", animals)