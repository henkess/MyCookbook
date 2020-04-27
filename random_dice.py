import random
run = True
while run:
    roll = random.randint(1, 6)
    rolled = input("press enter to continue, q to quit... ")
    if rolled == "q": run = False       # you can use break
    print(roll)

print("Thank you")


