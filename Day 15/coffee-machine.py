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

profit = 0
is_on = True


# TODO 4: Check resources sufficient?
def check_stock(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {ingredients[item]}")
            return False
    return True


# TODO 5: Process coins
def process_coins():
    print("=== Please insert coins ===")
    coins = int(input("How many quarters ($0,25): ")) * 0.25
    coins += int(input("How many dimes ($0,10): ")) * 0.1
    coins += int(input("How many nickles ($0,05): ")) * 0.05
    coins += int(input("How many pennies ($0,01): ")) * 0.01
    return coins


# TODO 6: Check transaction successful?
def transaction_successful(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money
        return True
    else:
        print("Sorry, not enough money. Money Refunded.")
        return False


# TODO 7: Make Coffee.
def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕")


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino)
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # TODO 3: Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(profit, 2)}")
    else:
        if MENU.get(choice) is not None:
            drink = MENU[choice]
            if check_stock(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
