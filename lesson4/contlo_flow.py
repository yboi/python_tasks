items = int(input("How many items: "))
days = int(input("How many days: "))

count = 1

while count <= days:
    items *= 2
    count += 1

result = items
print(result)

