from menu import MENU, resources

def is_resources_sufficient(order_ingredients):
    '''Return true is the resource is sufficient'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    '''Return the total coins from user input'''
    print("Please insert coin.")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.10
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''Return True when payment is accepted else return False'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_in_machine
        money_in_machine += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money has been refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

money_in_machine = 0
is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_in_machine}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])