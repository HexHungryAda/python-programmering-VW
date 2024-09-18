import math

cathetusA = 3
cathetusB = 4

hypothenuse = math.sqrt(cathetusA**2 + cathetusB**2)

print(f"The hypothenuse is {hypothenuse} length units.")

hypothenuse = 7.0
cathetusA = 5.0

cathetusB = math.sqrt(hypothenuse**2 - cathetusA**2)

print(f"The other cathetus is {round(cathetusB,1)} length units.")

# how round to one decimal for both of these? use round() eg round(x,decimals)
# also installed vim extension for vscode