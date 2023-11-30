from data import MENU, resources

# global variables
MONEY = 0
CURRENT_RESOURCES = resources.copy()
CURRENT_RESOURCES["money"] = MONEY


def printing_resource(resources):
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g")
    print(f"Money : ${resources["money"]}")


def check_resources(resources) -> bool:
    """This function checks whether resources are enough to make a drink"""
    for key in resources:
        if resources[key] <= 0:
            return False
    return True


#    resources["water"]


def coins_inserted() -> float:
    """this function sums the money inserted in """
    quarters = int(input("how many quarters you want to insert ? (type 0 if there is none) : "))
    dimes = int(input("how many dimes you want to insert ? : "))
    nickles = int(input("how many nickles you want to insert ? : "))
    pennies = int(input("how many pennies you want to insert ? : "))
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


def make_coffee(coffee_type, local_resources):
    local_resources['money'] += MENU[coffee_type]['cost']
    for key in local_resources:
        if key == 'money':
            continue
        local_resources[key] -= MENU[coffee_type]['ingredients'][key]
        if local_resources[key] < 0:
            print(f"Sorry there is not enough {key} ")
    return local_resources


def main():
    global MONEY, CURRENT_RESOURCES
    exit_loop = False
    while not exit_loop:
        response = input('What would you like? (espresso/latte/cappuccino):')
        if response == 'off':
            print("Thanks for using our machine 😊 😊")
            return 0
        elif response == 'report':
            printing_resource(CURRENT_RESOURCES)
        elif response == 'latte' or response == 'espresso' or response == 'cappuccino':
            insufficient_resource = check_resources(CURRENT_RESOURCES)
            if insufficient_resource:
                print(f"sorry there is not enough ingredients to make a {response} 🥲 🥲")
            else:
                # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

                print("please insert coins .")
                total = coins_inserted()
                if not affordable(total, response):
                    print("Sorry that's not enough money. Money refunded.")
                    return 0
                else:
                    print('here is your change : ', total - MENU[response]['cost'])
                    print(f"here is your {response} ☕ ☕")
                CURRENT_RESOURCES = make_coffee(response, CURRENT_RESOURCES)
                # return strings object of the resources left and store them in a variable


main()
