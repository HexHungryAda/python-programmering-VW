print("This program calculates the factorial of entered number")
n = int(input("Enter number: "))

product = 1
for i in range(1, n+1):
    product *= i
    if i != n:
        print(f"{i} * ",end="")
    else:
        print(i,end=" ")
print(f"= {product}")
