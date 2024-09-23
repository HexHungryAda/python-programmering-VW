class OutOfRangeError(Exception):
    pass

def get_float_input(prompt, min, max):
    while True:
        try:
            userInput = float(input(prompt))
            if not (min <= userInput <= max):
                raise OutOfRangeError(f"value must be between {min} and {max}")
            return userInput
        except ValueError as e:
            print("Error: ", e)
        except OutOfRangeError as e:
            print("Error: ", e) 

tramRides = get_float_input("How many times do you take the tram in one month? ", 0, 100)
ticketCost = get_float_input("How much does a ticket cost? (kr) ", 0, 300)
monthlyCardCost = get_float_input("How much does a monthly card cost? (kr) ", 0, 5000)

if ticketCost*tramRides < monthlyCardCost:
    print("Not worth it to buy a monthly card.")
elif ticketCost*tramRides == monthlyCardCost:
    print("It doesn't matter which option you pick, they are equally expensive.")
else:
    print("Worth it to get a monthly card.")

# I've demonstrated that I know how to do this, but if intended for general user would need errors to be more comprehensible. This would not require any further insight, just take time.
# ofc I suspect that the custom error class, should have the code inside of it, but I can learn this later when going through classes. so here I'm confused.