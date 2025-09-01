import textwrap

# MENU contains available coffee options.
# Each coffee type includes required ingredients with quantities
# and the cost of the coffee.
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

# Resource levels maximum capacity in the machine.
resources_capacity = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Current resource levels available in the machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

# Accepted coin types and their values in dollars.
coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

def coffee_machine():
    """Runs the main loop of the coffee machine.
    Prompts the user for input and processes commands:
    - 'espresso'/'latte'/'cappuccino' - order specific coffee from the list.
    - 'report' - report resources level.
    - 'refill' - refilling resources.
    - 'off' - turn the machine off.

    Available coffee options: 'espresso', 'latte', 'cappuccino'.
    """
    power_on = True
    coffee_choice = ["espresso", "latte", "cappuccino"]

    while power_on:
        user_command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_command in coffee_choice:
            refill_necessary = False

            # Check if machine has enough resources
            for ingredient, amount in MENU[user_command]["ingredients"].items():
                if amount > resources[ingredient]:
                    print(f"{ingredient.title()} level: refill needed")
                    refill_necessary = True
                else:
                    print(f"{ingredient.title()} level: OK")

            # If there is not enough resources, restart to the beginning and ask for refill
            if refill_necessary:
                print("Please refill mentioned resources.")
                continue

            # collect payment and give rest
            manage_payment(user_command)

            # make coffee
            print("your coffee is ready")

            # update resources
            for ingredient in MENU[user_command]["ingredients"]:
                resources[ingredient] -= MENU[user_command]["ingredients"][ingredient]
                print(f"Resource: {ingredient} reduced.")

        elif user_command == "report":
            report()
        elif user_command == "refill":
            refill()
        elif user_command == "off":
            power_on = False
        else:
            print("You typed wrong input, please try again.")

def report():
    """
    Prints the current levels of machine resources: water, milk, coffee, and money.
    """
    print(textwrap.dedent(f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money ${resources["money"]:.2f}
        """))

def refill():
    """
    Refill water, milk and coffee resources to their maximum capacity.
    """
    for resource in resources:
        if resource == "money":
            continue
        resources[resource] = resources_capacity[resource]
        print(f"Resource: {resource} refilled.")

def manage_payment(coffee):
    """Process payment.
    Prompts the user to insert coins until the full price is paid.
    Returns change if the user overpays.
    Updates the machine's money resource.
    """
    price = MENU[coffee]["cost"]
    while price > 0.00:
        coin_type = input(textwrap.dedent(f"""
            Amount to pay: ${price:.2f}.
            Quarter-0.25$
            Dime-0.10$
            Nickel-0.05$
            Penny-0.01$
            Type coin type you want to insert:
            """)).lower()

        if coin_type in coins:
            coin_amount = input(f"Type how many {coin_type}s you want to insert: ")
            if coin_amount.isdigit():
                price -= int(coin_amount) * coins[coin_type]
                price = round(price, 2)
            else:
                print("Input must be positive integer number.")
        else:
            print("You typed wrong input, try again.")

    if price < 0.00:
        print(f"You inserted too much. Here is your change: ${-price:.2f}")

    resources["money"] += MENU[coffee]["cost"]

if input("Type 'y' to turn ON coffee machine.").lower() == "y":
  coffee_machine()
else:
  print("Well, maybe next time...")

