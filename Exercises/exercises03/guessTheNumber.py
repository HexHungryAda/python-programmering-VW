import random as rng

max = 9999
min = 1000
number = rng.randint(1000, 9999)
guess = int((max+min) / 2)
guesses = 0

# it doesnt really go above 14 guesses, which seems about right log2(max-min)
for i in range(20):
    guesses += 1
    if guess == number:
        break
    elif guess < number:
        min = guess
        guess = int((guess + max) / 2)
    else:
        max = guess
        guess = int((guess + min) / 2)

print(f"The final guess is {guess}")
print(f"The number is {number}")
print(f"It took {guesses} guesses")