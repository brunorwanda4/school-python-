def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

given_number = int(input("Enter a number: "))
print(f"The factorial of {given_number} is {factorial(given_number)}")
