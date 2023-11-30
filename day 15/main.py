from data import MENU, resources


def check_resources() -> object:
    """This function checks whether resources are enough to make a drink"""
#    resources["water"]

def coins_inserted(quarters,dimes,nickles,pennies):
    """this function sums the money inserted in """
    print(coins_inserted())

def game():
    response = input('What would you like? (espresso/latte/cappuccino):')
    if response == 'off':
        return 0
    elif response == 'report':
        print(resources)
    elif response == 'latte':
        insufficient_resource = check_resources()
        if insufficient_resource:
            print(f"sorry there is not enough {insufficient_resource}")
        else :
            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

            print("please insert coins :")
            quarters = input("how many quarters you want to insert ? : ")
            dimes = input("how many dimes you want to insert ? : ")
            nickles = input("how many nickles you want to insert ? : ")
            pennies = input("how many pennies you want to insert ? : ")
            total = coins_inserted(quarters,dimes,nickles,pennies)


game()
