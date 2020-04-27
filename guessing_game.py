import random
# game set up 
print("welcome to the guessing game")
# user has 3 guesses before losing the game
guesses_number = 3
user_won = False
while guesses_number > 0:
    # computer guesses a number between 1 to 10
    corect_answer = random.randint(1,10)
    # user guesses the number
    user_guess = int(input("guess my number: "))
    # computer tells the user whether guess was too high or too low
    if user_guess == corect_answer:
        print("good guess")
        print("you are correct")
        user_won = True
        break
    elif user_guess < corect_answer: print("too low")

    elif user_guess > corect_answer: print("too high")
    guesses_number -= 1

if user_won == True: print("you won")
else: print("you lose")




