import random
randomint = random.randint(1, 100)

number = int(input("Welcome to the Guessing Game! Please input your desired number from 1-100: "))

while True:
    if number==randomint:
        print("It must be your lucky day, your guess is spot on! Congratulations!")
        break
    elif number<randomint:
        print("Your guess is too low! Try guessing higher")
    elif number>randomint:
        print("Your guess is too high! Try guessing lower")
    elif number>100:
        print("You need to guess 1-100 not higher than 100!")
    elif number<1:
        print("You need to guess 1-100 not any lower!")
    else:
        print("I dont even know what you did but u messed it up!")
