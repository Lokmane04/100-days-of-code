from data import MENU, resources


def check_resources() -> object:
    """This function checks whether resources are enough to make a drink"""


#    resources["water"]

def coins_inserted(quarters, dimes, nickles, pennies) -> float:
    """this function sums the money inserted in """
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def affordable(total, response):
    cost = MENU[response]['cost']
    if response == 'latte' and total >= cost:
        return True
    if response == 'cappuccino' and total >= cost:
        return True
    if response == 'espresso' and total >= cost:
        return True
    return False


def game():
    response = input('What would you like? (espresso/latte/cappuccino):')
    if response == 'off':
        return 0
    elif response == 'report':
        print(resources)
    elif response == 'latte' or response == 'espresso' or response == 'cappuccino':
        insufficient_resource = check_resources()
        if insufficient_resource:
            print(f"sorry there is not enough {insufficient_resource}")
        else:
            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

            print("please insert coins :")
            quarters = int(input("how many quarters you want to insert ? (type 0 if there is none) : "))
            dimes = int(input("how many dimes you want to insert ? : "))
            nickles = int(input("how many nickles you want to insert ? : "))
            pennies = int(input("how many pennies you want to insert ? : "))
            total = coins_inserted(quarters, dimes, nickles, pennies)
            if not affordable(total, response):
                print("Sorry that's not enough money. Money refunded.")
                return 0


game()
