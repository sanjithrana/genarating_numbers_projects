import random

top_of_range = input("Enter a number")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("please enter a number larger then 0")
        quit()
else:
    print("please enter a number..")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 1

while True:
    guesses += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    if user_guess == random_number:
        print("you got it!")
        break
    else:
        if user_guess > random_number:
            print("you got wrong")
            print("tou were above the number...")
        else:
            print("you were below the number")

print("you got it in "+str(guesses))