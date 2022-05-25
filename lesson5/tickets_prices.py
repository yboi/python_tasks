single_ticket = 100

passengers = int(input("How many people?: "))
loop_pessengers = 1
price = 0
while loop_pessengers <= passengers:
    age = int(input(f"What the age of {loop_pessengers} passenger?: "))
    if age > 3:
        price += single_ticket
    loop_pessengers += 1
print(f"The total price of {passengers} tickets will be ${price}")
