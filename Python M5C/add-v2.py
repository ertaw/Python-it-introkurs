
ducks = ["Huey", "Dewey", "Louie"]
composers = ["Mozart", "Bach"]


def add(prompt, strings):
    newString = str(input(prompt ))
    strings.append(newString)


ducks = ["Huey", "Dewey", "Louie"]

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()


composers = ["Mozart", "Bach"]
print(f" Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f" Composers: {composers}")
print()