
numbers = []
negative_count = 0

for i in range(4):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    if num < 0:
        negative_count += 1

if negative_count == 2:
    total_sum = sum(numbers)
    print(f"The sum of the numbers {numbers} is: {total_sum}")
else:
    print("You must enter exactly two negative numbers.")
