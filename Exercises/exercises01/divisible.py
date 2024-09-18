number = int(input("Enter a whole number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

if number % 5 == 0:
    print("Number is divisible by 5.")

if number % 5 == 0 and number % 2 != 0:
    print("Number is divisible by 5 and odd.")