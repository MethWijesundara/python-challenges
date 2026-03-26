import art
import menu_and_resources

profit = 0 
machine_on = True

# 2. check_resources() function
def check_resources(choice):
    for item, amount in menu_and_resources.MENU[choice]["ingredients"].items():
    # eg - MENU["latte"]["ingredients"].items() --> "water" : 200 , "milk" : 150 ...
        if amount > menu_and_resources.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    # compare required vs available 
    # return True if possible
    # return False if not
    # print what is missing

# 3. def process_coins():
def process_coins():
    """ Returns the total amount of coins inserted by the user."""
    print("Please insert coins.")
    total = 0
    try:
        total += int(input("How many quarters(0.25)? ")) * 0.25
        total += int(input("How many dimes(0.1)? ")) * 0.10
        total += int(input("How many nickles(0.05)? ")) * 0.05
        total += int(input("How many pennies(0.01)? ")) * 0.01
    except ValueError:
        print("Invalid number. Counting as 0.")
    return round(total,2)


# 4. def check_transaction():
def check_transaction(payment,cost):
    """Check if payment is enough. Update profit and give change if needed."""
    global profit

    if payment >= cost:
        change = round(payment - cost , 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# 5. def make_coffee():

def make_coffee(choice):
    """Deduct ingredients from resources and serve the coffee."""
    ingredients_needed = menu_and_resources.MENU[choice]["ingredients"]
    for item,amount in ingredients_needed.items():
        menu_and_resources.resources[item] -= amount 
    print(f"Here is your {choice} ☕. Enjoy!")


# 6. def print_report():

def print_report():
    print(f"Water: {menu_and_resources.resources['water']}ml")
    print(f"Milk: {menu_and_resources.resources['milk']}ml")
    print(f"Coffee: {menu_and_resources.resources['coffee']}g")
    print(f"Money: ${profit}")

print(art.logo)
# 1. main loop
while machine_on :
    
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
        print("(machine stops)")
    
    elif choice == "report":
        print_report()
    
    elif choice in menu_and_resources.MENU:
        if check_resources(choice):
            payment = process_coins()
            if check_transaction(payment,menu_and_resources.MENU[choice]["cost"]):
                make_coffee(choice)

    else:
        print("Invalid choice")