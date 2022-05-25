from main import resources, MENU


def report(water, milk, coffee, money_in_machine):
    print(f" Water: {water}ml\n Milk: {milk}ml\n Coffee: {coffee}g\n Money: ${money_in_machine}")


def check_resources(water, milk, coffee, user_choose):
    if MENU[user_choose]["ingredients"]["water"] > water:
        print("Sorry there is not enough water.")
        return False
    if MENU[user_choose]["ingredients"]["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        return False
    if user_choose in ("latte", "cappuccino"):
        if MENU[user_choose]["ingredients"]["milk"] > milk:
            print("Sorry there is not enough milk.")
            return False
    return True


def count_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    coins = float(format((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), ".2f"))
    return coins


def main():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    turn_off = True
    money_in_machine = 0
    while turn_off:
        user_choose = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choose == "turn off":
            turn_off = False
            return turn_off
        if user_choose in ("espresso", "latte", "cappuccino"):
            print(f"Your choice is {user_choose}")
            if check_resources(water, milk, coffee, user_choose):
                money = count_coins()
                if money > MENU[user_choose]["cost"]:
                    change = money - MENU[user_choose]["cost"]
                    print(f"Here is ${change} in change.\nHere is your {user_choose} ☕️. Enjoy!")
                elif money == MENU[user_choose]["cost"]:
                    print(f"Here is your {user_choose} ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
                money_in_machine += MENU[user_choose]["cost"]
                water -= MENU[user_choose]["ingredients"]["water"]
                coffee -= MENU[user_choose]["ingredients"]["coffee"]
                if user_choose in ("latte", "cappuccino"):
                    milk -= MENU[user_choose]["ingredients"]["milk"]
        if user_choose == "report":
            report(water, milk, coffee, money_in_machine)


main()

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
"""
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
"""
# TODO 3. Print report.
"""a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5"""
# TODO 4. Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""
# TODO 5. Process coins.
"""
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""
# TODO 6. Check transaction successful?
"""
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
"""
# TODO 7. Make Coffee.
"""
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""