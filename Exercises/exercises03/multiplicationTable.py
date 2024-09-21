for i in range(0,11):
    print(i * 6,end=" ")

print()
print()

table = int(input("Which table are you interested in? "))
start = int(input("Specify start of table: "))
endTable = int(input("Specify when table ends: "))

print(f"Your {table}th multiplcation table from {start} to {endTable}: ", end="")

for i in range(start,(endTable+1),1):
    print(i*table, end=" ")
print()

print()
print()

for i in range(0, 10+1):
    for j in range(0, 10+1, 1):
        print(f"{j*i :4}",end=" ")
    print()