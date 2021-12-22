MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# set profit equal to 0 at start
profit = 0

# create condition that is True for 'off' loop
machine_is_on = True

def process_coins():
    """add up money that was inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(payment, cost):
    """If payment was enough and there is enough resources, return True"""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients fromt he resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and False if ingredients are inefficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

while machine_is_on:
    # TODO: 1. Prompt user by asking what they would like
    coffee_selection = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    # TODO: 3. Print report of resources when prompted by 'report'
    if coffee_selection == "report":
        print(f'The machine has: \n{resources["water"]}mL of water \n{resources["milk"]}mL of milk \n{resources["coffee"]}g '
              f'of coffee \nMoney: ${profit}')
    # TODO: 2. Turn off machine when prompted by 'off'
    elif coffee_selection == "off":
        machine_is_on = False
    else:
        drink = MENU[coffee_selection]
        cost = drink["cost"]
        print(f"This drink cost: ${'{0:.2f}'.format(cost)}")

        # TODO: 4. Check if resources are sufficient for order
        if is_resource_sufficient(drink["ingredients"]):

            # TODO: 5. Process coins
            # Process coins for order and calculate change
            payment = process_coins()

            # TODO: 6. Check if transaction is successful
            if is_transaction_successful(payment, cost):

                # TODO: 7. Make the coffee
                make_coffee(coffee_selection, drink["ingredients"])