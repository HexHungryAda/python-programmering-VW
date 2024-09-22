import math

def euclidian_distance(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2) 

# don't really like this way of getting tuples from user. want to learn cleaner approach.
inputList = []
print("Enter 4 integers to represent 2 coordinate points: ")
for i in range(4):
    inputList.append(int(input("Enter a number: ")))

p = tuple(inputList[:2])
q = tuple(inputList[2:])

print(f"The euclidian distance between these points is about {round(euclidian_distance(p,q), 2)}")