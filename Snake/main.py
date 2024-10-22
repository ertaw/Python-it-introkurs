
from GameChecker import förlustCheck
from rita import ritaplan
from movementos import movement
from GameChecker import objectCollision
from generateApple import generateApple
from förkortaOrm import förkortaOrm



def main():
    spelplan = [["", "", "", "", ""],["", "", "", "", ""],["", "", "", "s","s"],["", "", "","",""],["", "", "", "",""]]
    snakeStart = [2,3]
    snakeEnd = [2,4]
    movementList = ["w"]
    generateApple(spelplan)

    while True:
        ritaplan(spelplan)
        snakeStart = movement(snakeStart,movementList)
        if förlustCheck(spelplan, snakeStart) == True:
            print("Du förlorade")
            break
        if objectCollision(spelplan, snakeStart, "a") == True:
            generateApple(spelplan)
        else:
            förkortaOrm(spelplan,snakeEnd,movementList)
        spelplan[snakeStart[0]][snakeStart[1]] = "s"

main()