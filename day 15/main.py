from data import MENU, resources

# global variables
MONEY = 0
CURRENT_RESOURCES = resources.copy()
CURRENT_RESOURCES["money"] = MONEY
print(CURRENT_RESOURCES)


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


def make_coffee(coffee_type, resources):
    for key in resources:
        resources[key] -= MENU[coffee_type][key]
        if resources[key] < 0:
            print(f"Sorry there is not enough {key} ")
    return resources


def game():
    global MONEY, CURRENT_RESOURCES
    exit_loop = False
    while not exit_loop:
        response = input('What would you like? (espresso/latte/cappuccino):')
        if response == 'off':
            exit_loop = True
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
                print(type(response))
                quarters = int(input("how many quarters you want to insert ? (type 0 if there is none) : "))
                dimes = int(input("how many dimes you want to insert ? : "))
                nickles = int(input("how many nickles you want to insert ? : "))
                pennies = int(input("how many pennies you want to insert ? : "))
                total = coins_inserted(quarters, dimes, nickles, pennies)
                if not affordable(total, response):
                    print("Sorry that's not enough money. Money refunded.")
                    return 0
                CURRENT_RESOURCES = make_coffee(response, CURRENT_RESOURCES)
                # return strings object of the resources left and store them in a variable


game()
