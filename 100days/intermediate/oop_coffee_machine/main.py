from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
from_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choosed_product = from_menu.get_items()
    user_choosed = input(f"What would you like? {choosed_product}: ")
    if user_choosed == "off":
        is_on = False
    elif user_choosed == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = from_menu.find_drink(user_choosed)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
