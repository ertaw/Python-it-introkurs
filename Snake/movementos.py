


def movement(snakeStart,movementList): #Funktion som förändrar koordinaten för ormens huvud men inte i själva spelplanen    
    while True:
        move = input("Choose move:")
        if move in("w", "a", "s", "d"):
            break
        else:            
            print("Please move using W, A, S, D")

    if(move == "w"):
        snakeStart[1] -= 1
        movementList.append("w")        
    elif(move == "a"):
        snakeStart[0] -=1
        movementList.append("a")
    elif(move == "s"):
        snakeStart[1] += 1
        movementList.append("s")
    elif(move == "d"):
        snakeStart[0] += 1
        movementList.append("d")
    return snakeStart
