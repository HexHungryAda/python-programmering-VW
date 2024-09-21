import random as rng

diceRolls = []
for i in range(10):
    diceRolls.append(rng.randint(1,6))

print(f"Unsorted: {diceRolls}")

diceRolls.sort()
print(f"Ascending order: {diceRolls}")

diceRolls.sort(reverse = True)
print(f"Descending order: {diceRolls}")

print(f"Maximum: {diceRolls[0]}")
print(f"Minimum: {diceRolls[-1]}")