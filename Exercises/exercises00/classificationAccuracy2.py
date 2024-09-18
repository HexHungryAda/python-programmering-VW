import math

truePostitive = 2
trueNegative = 985
falsePositive = 2
falseNegative = 11

modelAccuracy = (truePostitive + trueNegative) / (truePostitive + trueNegative + falsePositive + falseNegative)

print(f"The accuracy of this model is {modelAccuracy}.")

""" Not good model since when fire happens prediction is wrong 11/13. Sample size too low for everything except True negative.
Accuracy score misleading. """