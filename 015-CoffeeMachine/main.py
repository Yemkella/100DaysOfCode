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
    "money": 0,
}


machine_on = True


def off():
    exit()


def pay(cost):
    print("Please insert coins.")
    payment = 0
    quarters = int(input("How many quarters?: "))
    payment += quarters * .25
    dimes = int(input("How many dimes?: "))
    payment += dimes * .10
    nickels = int(input("How many nickels?: "))
    payment += nickels * .05
    pennies = int(input("How many pennies?: "))
    payment += pennies * .01
    if cost > payment:
        print("Sorry that's not enough money. Money refunded.")
    else:
        refund = payment - cost
        refund = '${:,.2f}'.format(refund)
        print(f"Here is {refund} in change.")
        resources['money'] += cost


def order():
    customer_order = ""
    while customer_order != 'espresso' and customer_order != 'latte' and customer_order != 'cappuccino' and customer_order != 'off':
        customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if customer_order == 'report':
            report()
        elif customer_order == 'off':
            off()
    drink = MENU[customer_order]
    cost = drink["cost"]
    ingredients = drink["ingredients"]
    water = ingredients["water"]
    if customer_order != 'espresso':
        milk = ingredients["milk"]
    else:
        milk = 0
    coffee = ingredients["coffee"]
    if water > resources['water']:
        print("Sorry there is not enough water.")
    elif milk > resources['milk']:
        print("Sorry there is not enough milk.")
    elif coffee > resources['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        pay(cost)
        brew(customer_order, water, milk, coffee)


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: {'${:,.2f}'.format(money)}")


def brew(customer_order, water, milk, coffee):
    print(f"Here is your {customer_order} ☕️. Enjoy!")
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee


while machine_on:
    order()
