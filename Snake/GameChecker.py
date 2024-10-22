from objectCollision import objectCollision

def förlustCheck(spelplan, snakeStart):
    for i in range(len(snakeStart)):        
        if (snakeStart[i] >= len(spelplan) or snakeStart[i] <= -1):            
            return True
    if (objectCollision(spelplan,snakeStart,"s") == True):
        return True
    else:   
        return False

