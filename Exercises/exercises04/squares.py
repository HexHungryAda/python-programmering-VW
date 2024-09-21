import matplotlib.pyplot as plt
import numpy as np

numbers = []
for i in range(-10,11):
    numbers.append(i)

squares = [x**2 for x in numbers]

print(squares)

xPoints = np.array([-10,10])
yPoints = np.array([0,100])
plt.plot(numbers, squares)
plt.savefig("sqaresPlot.png")