
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "tomato": 26,
}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3, "tomato": 20}


def uppercase(x):
    return x[0].upper() + x[1:]


name = input("""What is your name?: """)
print("Hi, %s, welcome to my fruit store. Here is the menu:" % (name))
print()

def check():
    mon = input()
    if input == "money":
     print(money)
def menu():
    for fruit in prices:
        print(uppercase(fruit))
        print("Price: $%s" % (prices[fruit]))
        print("Stock: %s" % (stock[fruit]))
        print()
    print("You have: $%s" % (money["cash"]))
    print()


def ask_fruit(money):
    fruit = input("""What fruit do you want?: """)
    print()

    if not fruit.lower() in stock:
        print("""Sorry, we don\'t have that, look at the menu.""")
        ask_fruit(money)
    elif stock[fruit.lower()] <= 0:
        print("""Sorry, %ss are out of stock""" % uppercase(fruit))
        ask_fruit(money)
    elif prices[fruit.lower()] > money["cash"]:
        print(f"You kidding me?! You can't even afford 1 {uppercase(fruit)}!\n")
        ask_fruit(money)
    else:
        ask_amount(fruit, money)


def ask_amount(fruit, money):
    amount = int(input("""How many %ss do you want?: """ % (fruit)))
    print()
    if amount <= 0:
        print("""At least buy one.""")
        ask_amount(fruit, money)
    elif stock[fruit.lower()] < amount:
        print("""Sorry, we don\'t have that many %ss.""" % (fruit))
        ask_amount(fruit, money)
    elif prices[fruit.lower()] * amount > money["cash"]:
        print(f"Your broke ass can't afford these {fruit}s!\n")
        ask_amount(fruit, money)
    else:
        sell(fruit, amount, money)


def sell(fruit, amount, money):
    cost = prices[fruit.lower()] * amount
    confirmation = input(
        """Are you sure? That will be $%s.
-Yes
-No
"""
        % (cost)
    ).lower()
    print()
    if confirmation == "yes":
        money["cash"] -= cost
        print("""Thank you for the business!""")
        stock[fruit.lower()] = stock[fruit.lower()] - amount
        ask_again()
    elif confirmation == "money":
        print(money)
    elif confirmation == "check money":
        ask_fruit(money)
    elif confirmation == "no":
        ask_fruit(money)
    else:
        print("""Answer me.""")
        sell(fruit, amount, money)


def ask_again():
    answer = input(
        """Do you want anything else?
-Yes
-No
-check money
"""
    ).lower()
    print()
    if answer.lower() == "check money":
        check()

        if input() == "money":
            print(money)

        
    if answer.lower() == "yes":
        menu()
        ask_fruit(money)
    elif answer.lower() == "no":
        print("Okay, bye.")
    else:
        print("Answer me.")
        ask_again()


money = {"cash": 132}
menu()
ask_fruit(money)
