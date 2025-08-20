#NUMBER GUESSING GAME 
import random
print("welcome to the number guessing game...")
print("guess the number that i have chosen btw 1-100")
print("you have only attempts")

secret_number=random.randint(1,100)
attempts=3
while True:
    guess=input("guess")
    if not guess.isdigit():
        print("try again :(")
        continue

    guess =int(guess)
    attempts+=1
    
    if guess < secret_number:
        print("low")
    elif guess>secret_number:
        print("high")
    else:
        print("congratulation you guess it right")
        break