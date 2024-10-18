def check_number_and_display(number):
    if number % 2 == 0:
        count = 0
        while count < 100:
            number -= 1
            print(number)
            count += 1
    else:
        count = 0
        while count < 50:
            number += 1
            print(number)
            count += 1

given_number = int(input("Enter a number: "))
check_number_and_display(given_number)
