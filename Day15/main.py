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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def final_esp():
    water_math = resources["water"] - MENU["espresso"]["ingredients"]["water"]
    coffee_math = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    resources["water"] = water_math
    resources["coffee"] = coffee_math

def final_lat():
    water_math = resources["water"] - MENU["latte"]["ingredients"]["water"]
    milk_math = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
    coffee_math = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    resources["water"] = water_math
    resources["milk"] = milk_math
    resources["coffee"] = coffee_math

def final_cap():
    water_math = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
    milk_math = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
    coffee_math = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
    resources["water"] = water_math
    resources["milk"] = milk_math
    resources["coffee"] = coffee_math


def payment(cost, final_order):
    global profit
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    penny = 0.01
    print("Please insert coins.")
    quarters_nr = float(input("How many quarters?: "))
    dimes_nr = float(input("How many dimes?: "))
    nickels_nr = float(input("How many nickels?: "))
    pennies_nr = float(input("How many pennies?: "))
    total_sum = quarters * quarters_nr + dimes * dimes_nr + nickels * nickels_nr + penny * pennies_nr

    if total_sum >= cost:
        change = total_sum - cost
        round_it_up = round(change, 2)
        profit += cost
        print(f"Here is your change: ${round_it_up}\n"
              f"Here is your {final_order}. Enjoy!")
        if final_order == "espresso":
            final_esp()
        elif final_order == "latte":
            final_lat()
        else:
            final_cap()
    else:
        print("Sorry, that's not enough money.\n"
              f"${total_sum} refunded.")

def espresso(coffee):
    price = MENU["espresso"]["cost"]
    if resources["water"] < 50:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < 18:
        print("Sorry, there is not enough coffee.")
    else:
        payment(price, coffee)

def latte(coffee):
    price = MENU["latte"]["cost"]
    if resources["water"] < 200:
        print("Sorry there is not enough water.")
    elif resources["milk"] < 150:
        print("Sorry, there is not enough milk.")
    elif resources["coffee"] < 24:
        print("Sorry, there is not enough coffee.")
    else:
        payment(price, coffee)

def cappuccino(coffee):
    price = MENU["cappuccino"]["cost"]
    if resources["water"] < 250:
        print("Sorry there is not enough water.")
    elif resources["milk"] < 100:
        print("Sorry, there is not enough milk.")
    elif resources["coffee"] < 24:
        print("Sorry, there is not enough coffee.")
    else:
        payment(price, coffee)

def report(money):
    money = money
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\n"
          f"Milk: {milk}ml\n"
          f"Coffee: {coffee}g\n"
          f"Money: ${money}")

ask_order = True

while ask_order:

    order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if order == "espresso":
        espresso(order)
    elif order == "latte":
        latte(order)
    elif order == "cappuccino":
        cappuccino(order)
    elif order == "report":
        report(profit)
    elif order == "off":
        ask_order = False
    else:
        print("You typed an invalid option.")