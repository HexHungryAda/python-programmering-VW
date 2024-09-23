import random as rng

diceRolls = []
for i in range(20):
    diceRolls.append(rng.randint(1,6))

with open("dice_rolls.txt", "w") as file:
    print("File created")
    file.write(f"Simulate 20 dice rolls: \n{diceRolls}\n\n")
    diceRolls.sort()
    file.write(f"Sorted dice rolls: \n{diceRolls}\n\n")
    file.write(f"Number of fours: {diceRolls.count(4)}\n\n")
print("File closed")