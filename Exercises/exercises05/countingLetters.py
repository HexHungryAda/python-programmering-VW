word = input("Enter a word: ")

upperCase = len([x for x in word if x.isupper()])
lowerCase = len([x for x in word if x.islower()])

print(f"There are {len(word)} letters in {word}. {upperCase} uppercase and {lowerCase} lowercase.")

""" obviously like many of my completed exercises doesn't handle strange user input cases or exceptions. 
Maybe add that later if consider it useful to develop the habit. """