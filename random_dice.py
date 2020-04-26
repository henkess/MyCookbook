import random
run = True
while run:
    roll = random.randint(1, 6)
    rolled = input("press enter to continue, q to quit... ")
    if rolled == "q": run = False
    print(roll)


