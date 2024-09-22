def name_cleaner(name):
    splitName = name.split()

    capitalizedName = []
    for i in splitName:
        capitalizedName.append(i.capitalize())

    cleanedName = " ".join(capitalizedName)
    return cleanedName

names = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "] 

for name in names:
    print(name_cleaner(name))