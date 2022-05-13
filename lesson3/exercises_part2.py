# 2
check_number = int(input("What number is\n"))
if check_number % 2 == 0:
    print(f"{check_number} is even")
else:
    print(f"{check_number} is odd")

# 2
number1 = int(input("Enter the first number\n"))
number2 = int(input("Enter the second number\n"))
if number1 * number2 > 500:
    print(f"sum is {number1 + number2}")

# 4
number1 = int(input("Enter the first number\n"))
number2 = int(input("Enter the second number\n"))
number3 = int(input("Enter the third number\n"))
numbers = [number1, number2, number3]
if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number3:
    print(number2)
else:
    print(number3)

checks = numbers[0]
for i in numbers:
    if i > checks:
        checks = i
print(checks)

# 5
number1 = int(input("Enter the first number\n"))
number2 = int(input("Enter the second number\n"))
number3 = int(input("Enter the third number\n"))
numbers = [number1, number2, number3]
if number1 == number2 and number2 == number3:
    print(number1 * len(numbers))
else:
    print(number1 + number2 + number3)
