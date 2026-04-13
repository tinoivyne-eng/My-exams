import random

# picks a random number
number=random(1, 100)

guess=34
attempts=0

print("Guess the number between 1 to 100 ")

# loop

while guess != number:
    guess=int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"Correct ")