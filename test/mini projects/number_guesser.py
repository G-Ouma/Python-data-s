import random

print("Welcome to Number guessing game!")

playing = input("Do you want to play (y/n)? ")
if playing.lower() != "y":
    quit()


max = input("Top of range (number): ")
if max.isdigit():
    max = int(max)
    if max <= 0:
        print("Enter a number > 0.")
        quit()    
else:
    print("Please enter a number!")
    quit()

random_number = random.randint(0, max) # type: ignore
guesses = 0

while True:
    guesses += 1 
    print("q to quit.")
    user = input("Guess a number: ")
    if user.isdigit():
        user = int(user)
        if user == random_number:
            print("You got it right!")
            break
        elif user > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")     
    elif user.lower() == "q":
        quit()
    else:
        print("Please enter a number!")

print("You got it right in", guesses, "guesses.")
