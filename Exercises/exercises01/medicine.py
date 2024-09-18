try:
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))
except ValueError:
    print("Enter numbers please.")

if age > 12:
    print("Take 1-2 pills.")
else:
    if weight > 25:
        print("Take 1/2-1 pill.")
    else:
        print("Take 1/2 pill.")