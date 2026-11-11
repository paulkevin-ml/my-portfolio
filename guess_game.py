import random
number = random.randint(1, 100)
attempts = 7

while attempts > 0:
    guess = int(input("Guess the number between 1 and 100: \n"))
    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")
    else:
        print("Guess is correct!")
        break
    attempts -=1