# converter temperature
degrees = int(input("Enter the temperature in degrees Celsius:\n"))
fahrenheit = 1.8 * degrees + 32
print(f"The temperature in degrees Fahrenheit is {fahrenheit}")

# Problem: Pure Gold!
pure_gold = int(input("How many K has your gold?\n"))
if pure_gold in (22, 24):
    print("Accepted")
else:
    print("Is not Accepted")

# Problem: At the boiling point!
temperature = int(input("What temperature of water?\n"))
if temperature >= 100:
    print("Boiling")
else:
    print("not yet")

# Problem: Leap year
year = int(input("What the year to check?\n"))
if (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")
elif (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Problem: Club Bouncer Code
age = int(input("What's your age?\n"))
name = input("What's your name?\n")
if age >= 18:
    print(f"Welcome {name}")
else:
    print("Sorry")

# Problem: 24K Magic


# Problem: Financial Transactions
bank = input("Please enter what the bank card you have\n")

if bank == "Visa" or bank == "Amex":
    print("accepted")

# Exercise: Equilateral triangle - isosceles
print("Please input length of the triangle: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

