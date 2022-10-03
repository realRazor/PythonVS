# Step 1

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

# Step 2
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Step 3
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return round(total,2)

# Step 4
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    print(f"you have inserted {money_received}")
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2) 
        if money_received>drink_cost:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
    

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        break
    elif choice == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")
    elif choice == "latte" or choice == "espresso" or choice =="cappuccino":
        print("Price: ",MENU[choice]["cost"])
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])
            
    else:
        print("Invalid enter! Try again! You can only select coffies!")
    
        