ladders = {9:34, 40:64, 67:86}
snakes = {54:19, 90:48, 99:77}
pos = 1
choice = 1
while choice != 0:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    elif pos+move == 100:
        print(f"You are now on square 100")
        print("You Win!")
        break
    elif pos+move > 100:
        print(f"You are now on square {pos}")
    else:
        pos+=move
        if pos in ladders:
            pos = ladders[pos]
        elif pos in snakes:
            pos = snakes[pos]
        print(f"You are now on square {pos}")