def calculate_bill(units):
    if units <= 50:
        bill = units * 75
    elif units <= 150:
        bill = (50 * 75) + (units - 50) * (75 * 0.95)
    elif units <= 175:
        bill = (50 * 75) + (100 * 75 * 0.95) + (units - 150) * (75 * 0.93)
    else:
        bill = (50 * 75) + (100 * 75 * 0.95) + (25 * 75 * 0.93) + (units - 175) * 75

    return bill

units_consumed = int(input("Enter the number of units consumed: "))
print(f"The electricity bill is {calculate_bill(units_consumed)} RWF")
