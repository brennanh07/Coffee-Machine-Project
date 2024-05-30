menu = [
    {
        "name": "espresso",
        "ingredients": {
            "water": 50,
            "beans": 10,
        },
        "price": 1.5,
    },
    {
        "name": "latte",
        "ingredients": {
            "water": 200,
            "beans": 24,
            "milk": 150,
        },
        "price": 2.5,
    },
    {
        "name": "cappuccino",
        "ingredients": {
            "water": 250,
            "beans": 24,
            "milk": 100,
        },
        "price": 3.0
    }
]

profit = 0
water = 300
milk = 200
beans = 100


def take_order():
    order = input("What would you like?: ").lower()
    if order == "report":
        return "report"
    elif order == "off":
        return "off"
    else:
        for y in range(len(menu)):
            if menu[y]["name"] == order:
                return y


def process_resource(coffee_order, ingredient):
    reduction_amount = int(menu[coffee_order]["ingredients"][ingredient])
    return reduction_amount


def take_payment():
    num_quarters = int(input("# of Quarters: "))
    num_dimes = int(input("# of Dimes: "))
    num_nickels = int(input("# of Nickels: "))
    num_pennies = int(input("# of Pennies: "))

    total = (num_quarters * .25) + (num_dimes * .10) + (num_nickels * .05) + (num_pennies * .01)

    return total


def process_payment(payment, coffee_order):
    order_price = menu[coffee_order]["price"]
    output = payment - order_price
    if payment > order_price:
        print(f"Your change is: ${output}")
    elif payment < order_price:
        while output < 0:
            print(f"Insufficient funds. You still owe: ${round((-1 * output), 2)}")
            payment = take_payment()
            output += payment

    else:
        print(f"Thank you!")


run = True

while run:
    print("Welcome to the coffee machine!")
    print("Here is the menu:\n")
    for x in range(len(menu)):
        print(f"{menu[x]['name']}... ${menu[x]['price']}0")

    menu_index = take_order()

    # Give report of amount of ingredients left if user enters "report" command
    if menu_index == "report":
        while menu_index == "report":
            print(f"Water: {water}ml")
            print(f"Beans: {beans}g")
            print(f"Milk: {milk}ml")
            menu_index = take_order()

    # Turn off if user enters "off" command
    if menu_index == "off":
        break

    # Check if enough ingredients left to make drink
    if menu[menu_index]["ingredients"]["water"] > water:
        print("Sorry, there's not enough water")
        break
    elif menu[menu_index]["ingredients"]["beans"] > beans:
        print("Sorry, there's not enough milk")
        break
    elif menu_index != 0:
        if menu[menu_index]["ingredients"]["milk"] > milk:
            print("Sorry, there's not enough milk")
            break

    water -= int(process_resource(menu_index, "water"))
    beans -= int(process_resource(menu_index, "beans"))
    if menu_index != 0:
        milk -= int(process_resource(menu_index, "milk"))

    print("Excellent choice! Please insert coins below.")

    total_payment = take_payment()

    process_payment(total_payment, menu_index)

    profit += int(menu[menu_index]["price"])

    print(f"Here is your {menu[menu_index]['name']}")
