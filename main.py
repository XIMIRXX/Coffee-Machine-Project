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
    "coffee": 100
}
profit = 0

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def money_insert():
    global quarters, dimes, nickles, pennies, quarter, dime, nickel, penny, us_money
    print("Insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    us_money = quarters * quarter + dimes * dime + nickles * nickel + pennies * penny
def calculate_money():
    global us_money, user_ask, profit
    if us_money < choice["cost"]:
        print("There is not enough money. Money refunded.")
    else:
        if us_money > choice["cost"]:
            print(f'Here is your change: ${us_money - choice["cost"]:.2f}')
        print(f"Here is your {user_ask} ☕️. Enjoy!")
        profit += choice["cost"]
def calculate_resources():
    global resources, user_ask
    for item in choice["ingredients"]:
        if choice["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            resources[item] -= choice["ingredients"][item]
    return True

is_on = True

while is_on:
    user_ask = input("What would you like?(espresso/latte/cappuccino): ")

    if user_ask == "off":
        is_on = False
    elif user_ask == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_ask == "espresso":
        choice = MENU[user_ask]
        if calculate_resources():
            money_insert()
            calculate_money()
    elif user_ask == "latte":
        choice = MENU[user_ask]
        if calculate_resources():
            money_insert()
            calculate_money()
    elif user_ask == "cappuccino":
        choice = MENU[user_ask]
        if calculate_resources():
            money_insert()
            calculate_money()
