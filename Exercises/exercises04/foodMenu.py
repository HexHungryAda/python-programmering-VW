foods = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
weekdays = ["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"]

foodMenu = []
for i in range(5):
    foodMenu.append(weekdays[i][:3]+": "+foods[i])

print("Bambameny")
for i in foodMenu:
    print(i)