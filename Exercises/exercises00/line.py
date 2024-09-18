import math

pointA = (4,4)
pointB = (0,1)

#Tuple can be accessed with index, durr.

slope = (pointA[1] - pointB[1]) / (pointA[0] - pointB[0])
# use point A.
yIntercept = pointA[1] - slope * pointA[0]

print(f"Slope is {slope}, y-intercept is {yIntercept}. Thus the full equation in slope-intercept form is y = {slope} + {yIntercept}.")