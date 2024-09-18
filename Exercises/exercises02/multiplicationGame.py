import random as rng

score = 0
playAgain = "y"

while (playAgain == "y"):
    x = rng.randint(1,10)
    y = rng.randint(1,10)
    answer = int(input(f"What is {x} times {y}? "))

    if answer == x*y:
        print("Good job <3")
        score += 1
    else:
        print(f"Wrong. Correct answer is {x*y}.")

    playAgain = input("Do you want to play again (y/n)? ")
    # how would I properly validate this?

print(f"Thank you for playing! Your score was {score}.")

# haven't added menu difficulty yet. can also optionally extend it at least with something.
