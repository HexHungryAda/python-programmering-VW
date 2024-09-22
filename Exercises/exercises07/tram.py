while (True):
    try:
        tramRides = float(input("How many times do you take the tram in one month? "))
    except ValueError:
        print("Number of times you take the tram must be between 0 and 100")
        print()
        continue
    try:
        ticketCost = float(input("How much does a ticket cost? (kr) "))
    except ValueError:
        print("Cost of a ticket has to be between 0 and 500")
    try:
        monthlyCardCost = float(input("How much does a monthly card cost? (kr) "))
    except ValueError:
        print("Cost of a monthly card has to be between 0 and 3000")
    break

if ticketCost*tramRides < monthlyCardCost:
    print("Not worth it to buy a monthly card.")
elif ticketCost*tramRides == monthlyCardCost:
    print("It doesn't matter which option you pick, they are equally expensive.")
else:
    print("Worth it to get a monthly card.")