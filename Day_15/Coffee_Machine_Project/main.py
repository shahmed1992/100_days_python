from sys import exit
resources_avail = {
    "water": 500,
    "milk": 500,
    "sugar": 500,
    "money":0
}
resources_required = {
    "espresso":{
        "ing":{
        "water": 75,
        "sugar": 25
        },
        "price": 1.5
    },
    "latte": {
        "ing": {
        "water": 50,
        "sugar": 25,
        "milk": 75
        },
        "price": 2.5
    },
    "cappuccino":{
        "ing":{
        "water": 75,
        "sugar": 25,
        "milk": 50
        },
        "price": 2
    }

}
def check_resources(drink):
    req_rsrcs = resources_required[drink]["ing"]
    for item, qty in req_rsrcs.items():
        # print(item, qty)
        if resources_avail[item] < qty:
            print(f"Sorry there is not enough {item}")
        else:
            # print(f"{item} is enough avail({qty}/{resources_avail[item]}) for {drink}")
            pass

def espresso():

    """
    1. Calculate profit and add it to the total_profit
    2. Deduct resources
    3.
    """
    resources_avail["money"]+=resources_required["espresso"]["price"]
    espresso_ingredients = resources_required["espresso"]["ing"]
    for item, qty in espresso_ingredients.items():
        resources_avail[item]-=qty

def latte():
    resources_avail["money"] += resources_required["latte"]["price"]
    espresso_ingredients = resources_required["latte"]["ing"]
    for item, qty in espresso_ingredients.items():
        resources_avail[item] -= qty
def cappuccino():
    resources_avail["money"] += resources_required["cappuccino"]["price"]
    espresso_ingredients = resources_required["cappuccino"]["ing"]
    for item, qty in espresso_ingredients.items():
        resources_avail[item] -= qty
def process_coins(drink):
    print("There are Enough Available Resources for the drink you selected.")
    print("Please insert coins")
    quarters = int(input("Enter no. of quarters:"))
    dimes = int(input("Enter no. of dimes:"))
    nickles = int(input("Enter no. of nickles:"))
    pennies = int(input("Enter no. of pennies:"))
    inserted_amount = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f"You have inserted {inserted_amount} $")
    if inserted_amount== resources_required[drink]["price"]:
        return 0
    elif inserted_amount > resources_required[drink]["price"]:
        # drink()
        user_balance = inserted_amount-resources_required[drink]["price"]
        return user_balance
        # print(f"Here is ${inserted_amount- resources_required[drink]["price"]} dollars in change")
    else:
        print(f"Amount provided is not Enough, required amount for "
              f"{drink} is {resources_required[drink]["price"]}$ ")
        return -1

def print_report():
    for item, qty in resources_avail.items():
        print(f" {item}: {qty}")

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    match user_input:
        case "espresso":
            check_resources("espresso")
            user_balance = process_coins("espresso")
            if user_balance>=0:
                print(f"Enjoy your Drink!!")
                espresso()
                if user_balance>0:
                    print(f"Here is your change of {user_balance} $ back")
        case "latte":
            check_resources("latte")
            user_balance = process_coins("latte")
            if user_balance>=0:
                print(f"Enjoy your Drink!!")
                latte()
                if user_balance>0:

                    print(f"Here is your change of {user_balance} $ back")
        case "cappuccino":
            check_resources("cappuccino")
            user_balance = process_coins("cappuccino")
            if user_balance>=0:
                print(f"Enjoy your Drink!!")
                cappuccino()
                if user_balance>0:
                    print(f"Here is your change of {user_balance} $ back")
        case "off":
            exit()
        case "report":
            print_report()

