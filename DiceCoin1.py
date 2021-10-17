import random


def cont():
    ask2 = input("Do You Want To Do This Again? Y/N ")
    if ask2 == "Y":
        dice_coin()
    elif ask2 == "N":
        print("ENDING PROGRAM")


def dice_coin():
    ask1 = input("Do You Want To Roll A Dice Or Flip A Coin? ")
    if ask1 == "Dice":
        rn = random.randint(1, 6)
        print("You Got " + str(rn) + "!")
        cont()
    elif ask1 == "Coin":
        rn = random.randint(1, 2)
        if rn == 1:
            print("Heads")
            cont()
        elif rn == 2:
            print("Tails")
            cont()
    else:
        print("Thing Not Found")


dice_coin()
