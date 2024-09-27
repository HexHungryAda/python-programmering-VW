import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
                print(f"Error: line {file.lineno} contains incorrect value type. Skipped.")


x = [t[0] for t in dataPoints]
y = [t[1] for t in dataPoints]
colors = ['red' if t[2] else 'blue' for t in dataPoints]

fileName = "pokemon_scatter_plot.png"
plt.scatter(x, y, c=colors)
plt.xlabel(dimensionLabels[0])
plt.ylabel(dimensionLabels[1])
plt.title("Pokemon scatter plot")
red_patch = mpatches.Patch(color="red", label="Pikachu")
blue_patch = mpatches.Patch(color="blue", label="Pichu")
plt.legend(handles=[red_patch, blue_patch])

plt.savefig(fileName)
print(f"{fileName} created")