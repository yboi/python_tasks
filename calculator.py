from art import logo1
print(logo1)

val1 = float(input("What the first number?: "))
print("""
  +
  -
  *
  /
""")

operation = input("Pick an operation: ")
val2 = float(input("What's the next value?: "))


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def multiply(val1, val2):
    return val1 * val2


def devide(val1, val2):
    return val1 / val2


if operation == "+":
    print(f"{val1} {operation} {val2} = {add(val1, val2)}")
elif operation == "-":
    print(f"{val1} {operation} {val2} = {subtract(val1, val2)}")
elif operation == "*":
    print(f"{val1} {operation} {val2} = {multiply(val1, val2)}")
elif operation == "/":
    print(f"{val1} {operation} {val2} = {devide(val1, val2)}")
else:
    print("Incorrect operation!")
