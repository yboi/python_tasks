from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)


def auction():
    answer = False
    bidders = {}
    while not answer:
        user_name = input("What's your name?\n")
        bid = float(input("What's your bid? $\n"))
        bidders[user_name] = bid
        will_continue = input("Are you the last of bidders? (yes or no)\n")
        if will_continue == "yes":
            answer = True
        elif will_continue == "no":
            clear()
        else:
            print("Error, you must use lowercase and only 'yes' or 'no'!")

    value = 0.00
    for person in (0, len(bidders) - 1):
        item = list(bidders.keys())[person]
        user_value = bidders.get(item)
    if user_value > value:
        value = user_value

    print(f"Winner is {item} where bid is $ {value}")

auction()
