

def förkortaOrm(spelplan,snakeEnd,movementList):
    spelplan[snakeEnd[0]][snakeEnd[1]] = ""
    if (movementList[0] == "w"):        
        snakeEnd[1] -= 1
    if (movementList[0] == "a"):
        snakeEnd[0] -= 1
    if (movementList[0] == "s"):
        snakeEnd[1] += 1
    if (movementList[0] == "d"):
        snakeEnd[0] += 1
    del movementList[0]