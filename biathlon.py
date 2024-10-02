from random import randint #importerar specifikt funktionen randint från biblioteket random
#slumpar 

#Slumpar träff eller miss. 1 är träff och 0 är miss
def shoot ():
    if (randint(1,10) > 0):
        return 1
    else:
        return 0

targets = ["*","*","*","*","*"]

#funktionen skriver ut listan på ett visst format
def printTargets(liststring):
    print ("1 2 3 4 5")
    for i in range(len(targets)):
        liststring = liststring + targets[i] + " "
    return liststring

#Använder funktionen shoot för att ändra i listan om shoot returnerar 1
def changeTargets(list, index):
    
    if shoot() == 1:
        if list[index - 1] == "0":
            print("hit on closed target\n")
        else:
            print("hit on open target\n")
            list[index - 1] = "0"       
    else:
        print("miss")
        

def aim(): #
    while True:
        try:
            number = int(input('Shot nr 1 at: '))
            print()
        except ValueError:
            print("Not a target!\n")
            continue
        if (number > 5 or number < 1):
            print("Not a target!\n")
            continue
        else:
            break
    return number

def play():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t     Biathlon\n")
    print("\ta hit or miss game\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("You got 5 shots \n")

    for i in range(5):
        print(printTargets("") + "\n")
        changeTargets(targets,aim())
    print(printTargets("") + "\n")


        

play()