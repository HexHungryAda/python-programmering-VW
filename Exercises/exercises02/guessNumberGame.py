import random as rng

number = rng.randint(1,100)
guess = 0
guesses = 0

print("Guess the number between 1 and 100.")

while (number != guess): # redundant due to break, but maybe more clear somehow. maybe reformat?
    try:
        guess = int(input("Enter guess: "))
    except ValueError:
        print("Enter a number please.")
    guesses += 1
    
    if number != guess:
        print("Your guess is wrong.")
        if number > guess:
            print("The number is higher than your guess.")
        else:
            print("The number is lower than your guess.")
    else:
        print(f"Your guess is correct, you win <3!. You made {guesses} guesses.")
        break

    # haven't implemented automatic guess algorithm yet, but seems simple enough. do I use a different file or overwrite?