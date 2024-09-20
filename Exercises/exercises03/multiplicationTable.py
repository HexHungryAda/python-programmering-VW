for i in range(0,11):
    print(i * 6,end=" ")

print()
print()

table = int(input("Which table are you interested in? "))
start = int(input("Specify start of table: "))
end = int(input("Specify when table ends: "))

print(f"Your {table}th multiplcation table from {start} to {end}: ", end="")

for i in range(start,(end*table+1),table):
    if i % table != 0:
        print(i,end=" ")
print()