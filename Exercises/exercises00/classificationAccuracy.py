import math

successes = 300
total = 365

# using basic laplace rule of succession to estimate classification accuracy. There are of course other alternatives.
ModelAccuracy = (successes + 1) / (total + 2)

# rounded to 3 decimal digits for display clarity. 
print(f"The accuracy of this model is {round(ModelAccuracy, 3)}.")
