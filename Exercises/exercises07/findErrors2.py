def is_fourdigit(number):
    number = abs(number)
    if number // 1000 < 10 and number > 999:
        return True
    else:
        return False

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")