import math

pointA = (2,1,4)
pointB = (3,1,0)

squaredDifference = 0
for i in range(len(pointA)):
    squaredDifference += (pointB[i]-pointA[i])**2
distance = math.sqrt(squaredDifference)

print(f"The distance is about {round(distance, 2)} l.u.")

#Used the loop since generalises to n-dimensions.
#Pretty sure that this is not according to style convention.