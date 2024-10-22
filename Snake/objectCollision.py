
def objectCollision(spelplan, snakeStart, value):
    if(spelplan[snakeStart[0]][snakeStart[1]] == value):
        return True
    else:
        return False