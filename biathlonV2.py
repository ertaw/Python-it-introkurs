from random import randint #importerar specifikt funktionen randint från biblioteket random
#slumpar 

#Slumpar träff eller miss. 1 är träff och 0 är miss
def shoot ():
    if (randint(1,10) > 0):
        return 1
    else:
        return 0

#Globala variabler
targets1 = ["*","*","*","*","*"]
targets2 = ["*","*","*","*","*"]
player1 = ["",""]
player2 = ["",""]


#funktionen skriver ut listan på ett visst format
def printTargets(liststring, index):
    
    if (index == 1):
            print(player1[0])
            print ("1 2 3 4 5")
            for i in range(len(targets1)):
                liststring = liststring + targets1[i] + " "
    else:
            print(player2[0])
            print ("1 2 3 4 5")
            for i in range(len(targets2)):
                liststring = liststring + targets2[i] + " "
    return liststring


#test
#Använder funktionen shoot för att ändra i listan om shoot returnerar 1
def changeTargets(list, index, turnindex, score):
    
    if shoot() == 1:
        if list[index - 1] == "0":
            print("hit on closed target\n")
            return score
        else:
            print("hit on open target\n")
            list[index - 1] = "0"
            return score + 1


     
    else:
        print("miss")
        

def aim(): #Funktion för att välja 
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

#Ritar ut start texten
def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t     Biathlon\n")
    print("\ta hit or miss game\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")



def play():
    score1 = 0
    score2 = 0
    turn = 1
    print("You got 5 shots \n")
    for i in range(10):
        if turn == 1:
            print(printTargets("", turn) + "\n")
            score1 = changeTargets(targets1, aim(), turn, score1)
            turn = 2
        elif turn == 2:
            print(printTargets("", turn) + "\n")
            score2 = changeTargets(targets2,aim(), turn, score2)
            turn = 1
    
    print("Player " + player1[0] + " score: " + str(score1))
    print("Player " + player2[0] + " score: " + str(score2))
    #print(printTargets("Player: " + player1[0] + ": ", 1) + "\n")
    #print(printTargets("Player: " + player2[0] + ": ", 2) + "\n")


def menu():
    splash()
    print("choose name for player 1")
    player1[0] = input()
    print("choose name for player 2")
    player2[0] = input()
    play()

menu()

#förbättringsmöjligheter
#Vinst text om man sätter alla skott
#Välja antal personer som kan skjuter och dem har olika 