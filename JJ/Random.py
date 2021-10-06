import random
randomint = random.randint(1, 100)
rtries = 10

while rtries>0:
    tries = 10-rtries
    number = int(input("Welcome to the Guessing Game! You have 10 tries! Please input your desired number from 1-100: "))
    if number==randomint:
        if rtries>8:
            print(f"Your guess is spot on! It only took you {tries} tries, Congratulations!")
        elif rtries>3:
            print(f"Your guess is spot on! It took you {tries} tries. Congratulations!")
        else:
            print(f"You almost lost but u still won in the end! it took you {tries} tries, Congratulations! ")
        break
    elif number>100:
        print("You need to guess 1-100 not higher than 100!")
        rtries-=1
    elif number<1:
        print("You need to guess 1-100 not any lower!")
        rtries-=1
    elif number<randomint:
        print("Your guess is too low! Try guessing higher")
        rtries-=1
    elif number>randomint:
        print("Your guess is too high! Try guessing lower")
        rtries-=1
    else:
        print("I dont even know what you did but u messed it up!")i
        rtries-=1

if rtries==0:
    print("You ran out of tries! Restart the game to try again")