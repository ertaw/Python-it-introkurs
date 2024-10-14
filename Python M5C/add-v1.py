
ducks = ["Huey", "Dewey", "Louie"]

def add():
    print("List of ducks:", ducks)
    newDuck = str(input("Add a duck: " ))
    ducks.append(newDuck)
    print("Updated list of ducks:", ducks )

add()

