from coffee_maker.menu import Menu, MenuItem
from coffee_maker.coffee_maker import CoffeeMaker
from coffee_maker.money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
EXIT = False
RESPONSE=''


def main():
    global EXIT, RESPONSE
    print(RESPONSE)
    while not EXIT:
        RESPONSE = input(f"What would you like? : ({menu.get_items()}) ")
        if RESPONSE == 'report':
            coffee_machine.report()
        elif RESPONSE == 'off':
            EXIT = True
        else:
            drink = menu.find_drink(RESPONSE)
            coffee_machine.is_resource_sufficient(drink)
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)


main()




