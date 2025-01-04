import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif user_input == "off":
        sys.exit()
    else:
        menuItem = menu.find_drink(user_input)
        resource_suff = coffeeMaker.is_resource_sufficient(menuItem)
        if resource_suff:
            payment_status = moneyMachine.make_payment(menuItem.cost)
            if payment_status:
                coffeeMaker.make_coffee(menuItem)
