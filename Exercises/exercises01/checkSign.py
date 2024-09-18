number = float(input("Enter a number: "))
# not inputting a number breaks the program of course.
# doesn't look clean with the rounding.
# how to make it compatible with 'bash-arguments'?

print(f"{round(number, 3)} is ", end="")
if number > 0:
    print("postitive.")
elif number < 0:
    print("negative.")
else:
    print("zero.")