print("Enter information about your luggage.")
try:
    weight = float(input("Enter weight: "))
    dimensions = (float(input("Enter length, width, height: \n")), float(input()), float(input()))
except ValueError:
    print("Please enter numbers.")

# how would one prevent the newlines here with the input()?
# mind is blanking out for a better name than "dimensions". Also possibly more clarity if just label each dimension.
# still quite unsure what to actually do with this exception thingy.

if weight <= 8 and dimensions[0] <= 55 and dimensions[1] <= 40 and dimensions[2] <= 23:
    print("Luggage is allowed <3")
else:
    print("Luggage is not allowed.")