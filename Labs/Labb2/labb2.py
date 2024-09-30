import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

file_path = "Data/datapoints.txt"
data_points = []
dimension_labels = ""

with open(file_path, "r") as file:
    dimension_labels = file.readline().strip().split(',')
    lastLabel = dimension_labels.pop()
    dimension_labels[-1] = dimension_labels[-1] + "," + lastLabel 

    for line in file:
        numbers = line.strip().split(',')
        if len(numbers) == 3:
            try:
                data_points.append((float(numbers[0]), float(numbers[1]), bool(int(numbers[2]))))
            except ValueError:
                print(f"Error: line contains incorrect value type. Skipped.")

data_array = np.array(data_points)

x_values = data_array[:, 0]
y_values = data_array[:, 1]
pokemon_type = data_array[:, 2]

fileName = "pokemon_scatter_plot.png"
plt.title("Pokemon scatter plot")
plt.xlabel(dimension_labels[0])
plt.ylabel(dimension_labels[1])

red_patch = mpatches.Patch(color="red", label="Pikachu")
blue_patch = mpatches.Patch(color="blue", label="Pichu")
plt.legend(handles=[red_patch, blue_patch])

plt.scatter(x_values, y_values, c=pokemon_type, cmap="bwr")

plt.savefig(fileName)
print(f"{fileName} created")

test_points = []
file_path = "Data/testpoints.txt"

with open(file_path, "r") as file:
    file.readline() #skip the first line.

    for line in file:
        line_parts = line.strip().split('.', 1)
        data_parts = line_parts[1]
        numbers = data_parts.strip().replace('(', "").replace(')', "").split(',')
        if len(numbers) == 2:
            try:
               test_points.append((float(numbers[0]), float(numbers[1])))
            except ValueError:
                print(f"Error: line contains incorrect type. Skipped.")

test_array = np.array(test_points)

def classify_pokemon(test_point):

    shortest_distance = float('inf')
    closest_point_index = None

    for i in range(len(data_array)):
        distance = np.linalg.norm(data_array[i, :2] - test_point)
        if distance < shortest_distance:
            shortest_distance = distance
            closest_point_index = i

    closest_point = data_array[closest_point_index]

    if closest_point[2] == 0:
        print(f"Testpoint {test_point} classified as Pichu")
    else:
        print(f"Testpoint {test_point} classified as Pikachu")

def classify_pokemon_voting(test_point):
    distances = np.linalg.norm(data_array[:, :2] - test_point[np.newaxis, :], axis=1) # if not newaxis then get only one value 
    closest_points = np.zeros((10,2))
    closest_points[:, 0] = np.inf

    for i, distance in np.ndenumerate(distances):
        if distance < closest_points[-1, 0]: # get the largest distance.
            closest_points[-1] = [distance, i[0]] # just i gives eg (0, ) 
            closest_points = closest_points[closest_points[:, 0].argsort()] # array[indices] to get the sorted array.
    
    closest_points = data_array[closest_points[:, 1].astype(int)] # need into or bool indices 

    pikachu_counter = np.count_nonzero(closest_points[:, 2]) # count number of true values i.e pikachu

    print(f"Testpoint {test_point} classified as ", end="")
    if pikachu_counter > 5:
        print("Pikachu")
    elif pikachu_counter == 5:
        # tie resolved by considering closest point.
        if closest_points[0, 2] == 0:
            print("Pichu")
        else:
            print("Pikachu")
    else:
        print("Pichu")

for test_point in test_array:
    classify_pokemon(test_point)

print("majority voting:")
for test_point in test_array:
    classify_pokemon_voting(test_point)

def get_float_input(prompt):
    while True:
        try:
            userInput = float(input(prompt))
            return userInput
        except ValueError as e:
            print("Error: ", e)

print("You are entering a 2D testpoint, limited to float numbers e.g 3.42, 5")
test_point = np.array((get_float_input("Enter x coordinate: "), get_float_input("Enter y coordinate: ")))

classify_pokemon(test_point)

print("majority voting: ")
classify_pokemon_voting(test_point)