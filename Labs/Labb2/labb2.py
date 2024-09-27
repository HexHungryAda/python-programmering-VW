import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

filePath = "Data/datapoints.txt"
dataPoints = []
dimensionLabels = ""

with open(filePath, "r") as file:
    dimensionLabels = file.readline().strip().split(',')
    lastLabel = dimensionLabels.pop()
    dimensionLabels[-1] = dimensionLabels[-1] + "," + lastLabel 

    for line in file:
        numbers = line.strip().split(',')
        if len(numbers) == 3:
            try:
                dataPoints.append((float(numbers[0]), float(numbers[1]), bool(int(numbers[2]))))
            except ValueError:
                print(f"Error: line contains incorrect value type. Skipped.")
                # how do error about specific line number? how deal with this stuff in general? 

data_array = np.array(dataPoints)

x_values = data_array[:, 0]
y_values = data_array[:, 1]
pokemon_type = data_array[:, 2]

fileName = "pokemon_scatter_plot.png"
plt.title("Pokemon scatter plot")
plt.xlabel(dimensionLabels[0])
plt.ylabel(dimensionLabels[1])

red_patch = mpatches.Patch(color="red", label="Pikachu")
blue_patch = mpatches.Patch(color="blue", label="Pichu")
plt.legend(handles=[red_patch, blue_patch])

plt.scatter(x_values, y_values, c=pokemon_type, cmap="bwr")

plt.savefig(fileName)
print(f"{fileName} created")

test_points = []
filePath = "Data/testpoints.txt"

with open(filePath, "r") as file:
    file.readline() #skip the first line.

    for line in file:
        line_parts = line.strip().split('.', 1)
        data_parts = line_parts[1]
        numbers = data_parts.strip().replace('(', "").replace(')', "").split(',')
        if len(numbers) == 2:
            try:
               test_points = tuple(map(float, numbers))
            except ValueError:
                print(f"Error: line contains incorrect type. Skipped.")
        print(numbers)

for point in test_points:
    print(point, end=" ")
print()
print(type(test_points[0]))
print(type(test_points))