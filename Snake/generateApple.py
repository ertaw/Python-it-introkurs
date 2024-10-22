import random
from GameChecker import objectCollision
def generateApple(spelplan):
    while True:        
        posY = random.randint(0,4)
        posX = random.randint(0,4)
        coordinate = [posX, posY]
        if (objectCollision(spelplan,coordinate,"s") == False):
            spelplan[coordinate[0]][coordinate[1]] = "a"
            break

