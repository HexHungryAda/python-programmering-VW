print("The angles should make up a triangle.")
try:
    angle1 = float(input("Enter an angle: "))
    angle2 = float(input("Enter another angle: "))
    angle3 = float(input("Enter another angle: "))
except ValueError:
    print("Invalid input, please enter only numbers.")

# This should of course loop until user inputs correctly. but not doing this for now.

# will the float mess up the comparison? doesn't seem to but who knows.
if angle1 + angle2 + angle3 == 180:
    if (angle1 or angle2 or angle3) == 90:
        print("The triangle has a right angle.")
    else:
        print("The triangle doesn't have a right angle.")
else:
    print("This is not a triangle.")