import matplotlib.pyplot as plt

def function(x):
    return x**2-3
def function2(x):
    return 4*x-7

xPoints = []
yPoints = []
for x in range(-10, 11):
    xPoints.append(x)
    yPoints.append(function(x))

xPoints2 = []
yPoints2 = []
for x in range(-10, 11):
    xPoints2.append(x)
    yPoints2.append(function2(x))

plt.plot(xPoints, yPoints)
plt.plot(xPoints2, yPoints2)
plt.savefig("mathematicalFunctions.png")

print("Check the image file to see the graph")

# function2 is the derivative of function durr