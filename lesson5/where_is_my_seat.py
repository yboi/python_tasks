seats = [
    ["a", "b"],
    ["c", "d"],
    ["e", "f"],
    ["g", "h"],
]
row = int(input("please chose row: ")) - 1
seat = int(input("please chose number of seat: ")) - 1

try:
    print(seats[row][seat])
except IndexError:
    print("is not correct place")
