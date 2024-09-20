sum = 0
for i in range(1,101):
    sum += i
    if i == 100:
        print(f"{i}",end="")
    else:
        print(f"{i}+",end="")
print(f"={sum}")

# is there a cleaner way to format it correctly rather than using the if-else?
print()

sum = 0
for i in range(1,100,2):
    sum += i
    if i == 100:
        print(f"{i}",end="")
    else:
        print(f"{i}+",end="")
print(f"={sum}")