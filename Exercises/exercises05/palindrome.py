word = input("Enter a sequence of characters: ")
modifiedWord = word.lower().replace(" ", "")
reversed = modifiedWord[::-1] 

palindrome = True
for i in range(len(modifiedWord)):
    if modifiedWord[i] != reversed[i]:
        palindrome = False

if palindrome == True:
    print(f"{word} is a palindrome.")
else: print(f"{word} is not a palindrome.")