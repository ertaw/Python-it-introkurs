


def ritaplan(spelplan): #Funktion för att rita ut spelplanen. Ändrar inget, printar bara
    for y in range(len(spelplan)):
        tempstring = ""
        for x in range(len(spelplan)):
            if spelplan[x][y] == "":
                tempstring += "*  "
            elif spelplan[x][y] == "s":
                tempstring += "s  "
            elif spelplan[x][y] == "a":
                tempstring += "a  "
        print (tempstring)

    print()
