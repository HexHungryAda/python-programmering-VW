import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def get_float_input(prompt):
    while True:
        try:
            userInput = float(input(prompt))
            return userInput
        except ValueError as e:
            print("Error: ", e)

def classify_pokemon(test_feature, test_label=None):
    # use numpy library to calculate euclidian distance and do majority voting on the 10 closest points.
    # if tie then closest point is prioritized.
    # also returns np.bool if prediction matches test_label. if no label None.
     
    prediction = None
    distances = np.linalg.norm(train_array[:, :2] - test_feature[np.newaxis, :], axis=1) # if not newaxis then get only one value 
    closest_points = np.zeros((10, 2))
    closest_points[:, 0] = np.inf

    for i, distance in np.ndenumerate(distances):
        if distance < closest_points[-1, 0]: # get the largest saved distance and compare it.
            closest_points[-1] = [distance, i[0]] # just i gives eg (0, ) 
            closest_points = closest_points[closest_points[:, 0].argsort()] # array[indices] to get the sorted array.
    
    closest_points = train_array[closest_points[:, 1].astype(int)] # need into or bool indices 

    pikachu_counter = np.count_nonzero(closest_points[:, 2])

    print(f"Testpoint {dimension_labels[0]}, {dimension_labels[1]}: {test_feature} classified as ", end="")
    if pikachu_counter > 5:
        print("Pikachu")
        prediction = True
    elif pikachu_counter == 5:
        if closest_points[0, 2] == 0:
            print("Pichu")
            prediction = False
        else:
            print("Pikachu")
            prediction = True
    else:
        print("Pichu")
        prediction = False

    if test_label is not None:
        return prediction == test_label 
    else:
        return None

#-----------------gettting data from files----------------
file_path = "Data/datapoints.txt"
data_points = []
dimension_labels = ""

with open(file_path, "r") as file:
    dimension_labels = file.readline().strip().split(',')
    lastLabel = dimension_labels.pop()
    dimension_labels[-1] = dimension_labels[-1] + "," + lastLabel 
    dimension_labels[0] = dimension_labels[0].replace("(", "", 1)

    for line in file:
        numbers = line.strip().split(',')
        if len(numbers) == 3:
            try:
                data_points.append((float(numbers[0]), float(numbers[1]), bool(int(numbers[2]))))
            except ValueError:
                print(f"Error: line contains incorrect value type. Skipped.")

data_array = np.array(data_points)

train_array = data_array

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

testfile_array = np.array(test_points)

#----------------scatterplot-----------------
x_values = data_array[:, 0]
y_values = data_array[:, 1]
pokemon_type = data_array[:, 2]

file_name = "pokemon_scatter_plot.png"
plt.title("Pokemon scatter plot")
plt.xlabel(dimension_labels[0])
plt.ylabel(dimension_labels[1])

red_patch = mpatches.Patch(color="red", label="Pikachu")
blue_patch = mpatches.Patch(color="blue", label="Pichu")
plt.legend(handles=[red_patch, blue_patch])

plt.scatter(x_values, y_values, c=pokemon_type, cmap="bwr")

plt.savefig(file_name)
print(f"Created file: {file_name}", end="\n\n")
plt.clf()

#------------pokemon classification------------
print("Classifying testpoints from the testpoints file:")
for test_feature in testfile_array:
    classify_pokemon(test_feature)
print()


overall_accuracy = []
for i in range(10):
    pikachu_array = data_array[data_array[:, 2] == 1]
    pichu_array = data_array[data_array[:, 2] == 0]
    np.random.shuffle(pichu_array)
    np.random.shuffle(pikachu_array)
    train_array = np.concatenate((pichu_array[:50, :], pikachu_array[:50, :]))
    test_array = np.concatenate((pichu_array[50:, :], pikachu_array[50:, :]))
    np.random.shuffle(train_array)
    np.random.shuffle(test_array)
    test_features = test_array[:, :2]
    test_labels = test_array[:, 2]

    accuracy_array = np.empty(len(test_features), dtype=object)

    print("Classifying testpoints extracted randomly from the datapoints file: ")
    for i, (test_feature, test_label) in enumerate(zip(test_features, test_labels)):
        accuracy_array[i] = classify_pokemon(test_feature, test_label)
    accuracy = np.sum(accuracy_array.astype(bool)) / len(accuracy_array) # assuming no None value bugs 
    overall_accuracy.append(accuracy)
    print(f"accuracy score: {accuracy}", end="\n\n")

mean_accuracy = np.mean(overall_accuracy)
print(f"Average accuracy over 10 runs: {mean_accuracy}")


file_name = 'prediction_accuracy_plot.png'
plt.title('Accuracy over 10 runs')
plt.xlabel('Run')
plt.ylabel('Accuracy')
plt.ylim(0, 1.02) # slightly above 1 to prevent cut-off if 1.0 score 
plt.plot(overall_accuracy, marker='o')
plt.xticks(np.arange(len(overall_accuracy)), np.arange(1, len(overall_accuracy) + 1))
plt.savefig(file_name)
print(f"Created file: {file_name}", end="\n\n")


print(f"Enter testpoint coordinates for a pokemon {dimension_labels[0]},{dimension_labels[1]}.\nOnly float allowed e.g 3.5, 5")
test_feature = np.array((get_float_input("Enter x coordinate: "), get_float_input("Enter y coordinate: ")))
classify_pokemon(test_feature)