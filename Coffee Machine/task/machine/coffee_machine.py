water = 400
milk = 540
beans = 120
cups = 9
money = 550
action = ''

# espresso
water_for_one_cup_espresso = 250
beans_for_one_cup_espresso = 16
price_for_one_cup_espresso = 4

# latte
water_for_one_cup_latte = 350
beans_for_one_cup_latte = 20
milk_for_one_cup_latte = 75
price_for_one_cup_latte = 7

# cappuccino
water_for_one_cup_cappuccino = 200
beans_for_one_cup_cappuccino = 12
milk_for_one_cup_cappuccino = 100
price_for_one_cup_cappuccino = 6


def machine_state():
    print()
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print("$"+ str(money), "of money")
    print()


def check_qty(type):
    global money, water, milk, beans, cups
    qty_water = qty_milk = qty_beans = 0

    if type == '1':
        qty_water = water_for_one_cup_espresso
        qty_milk = 0
        qty_beans = beans_for_one_cup_espresso
    elif type == '2':
        qty_water = water_for_one_cup_latte
        qty_milk = milk_for_one_cup_latte
        qty_beans = beans_for_one_cup_latte
    elif type == '3':
        qty_water = water_for_one_cup_cappuccino
        qty_milk = milk_for_one_cup_cappuccino
        qty_beans = beans_for_one_cup_cappuccino

    if (water > qty_water) and (milk > qty_milk) and (beans > qty_beans):
        print("I have enough resources, making you a coffee!")
        print()
        # print("For", qty_cup_coffee, "cups of coffee you will need:")
        # print(qty_water, "ml of water")
        # print(qty_milk, "ml of milk")
        # print(qty_beans, "g of coffee beans")
        return True

    else:
        if water < qty_water:
            print("Sorry, not enough water!")
        elif milk < qty_milk:
            print("Sorry, not enough water!")
        elif beans < qty_beans:
            print("Sorry, not enough water!")
        elif cups <= 0:
            print("Sorry, not enough disposable cups!")
        return False


def buy():
    global money, water, milk, beans, cups
    print()
    option = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino or back to return:"))
    if option != 'back':
        if check_qty(option):
            if option == '1':
                # For one espresso,
                # the coffee machine needs 250 ml of water
                # and 16 g of coffee beans. It costs $4.
                money += price_for_one_cup_espresso
                water -= water_for_one_cup_espresso
                beans -= beans_for_one_cup_espresso
                cups -= 1
            elif option == '2':
                # For a latte,
                # the coffee machine needs 350 ml of water,
                # 75 ml of milk, and 20 g of coffee beans.
                # It costs $7.
                money += price_for_one_cup_latte
                water -= water_for_one_cup_latte
                milk -= milk_for_one_cup_latte
                beans -= beans_for_one_cup_latte
                cups -= 1
            elif option == '3':
                # for a cappuccino,
                # the coffee machine needs 200 ml of water,
                # 100 ml of milk, and 12 g of coffee.
                # It costs $6.
                money += price_for_one_cup_cappuccino
                water -= water_for_one_cup_cappuccino
                milk -= milk_for_one_cup_cappuccino
                beans -= beans_for_one_cup_cappuccino
                cups -= 1
        else:
            pass
    else:
        pass


def fill():
    global money, water, milk, beans, cups
    qty_fill_water = int(input("Write how many ml of water do you want to add:"))
    qty_fill_milk = int(input("Write how many ml of milk do you want to add:"))
    qty_fill_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    qty_fill_cups = int(input("Write how many disposable cups of coffee do you want to add"))
    water += qty_fill_water
    milk += qty_fill_milk
    beans += qty_fill_beans
    cups += qty_fill_cups


def take():
    global money
    print()
    print("I gave you $", money)
    print()
    money = 0


while action != "exit":
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "exit":
        break
        print(n)
    elif action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        machine_state()

"""
qty_cup_coffee = int(input("Write how many cups of coffee you will need: "))

# calcs
qty_water = qty_cup_coffee * 200
qty_milk = qty_cup_coffee * 50
qty_beans = qty_cup_coffee * 15


if (water / 200) > 1.0:
    qty_possible_water = math.ceil(int(water / 200))
else:
    qty_possible_water = int(water / 200)

if (milk / 50) > 1.0:
    qty_possible_milk = math.ceil(int(milk / 50))
else:
    qty_possible_milk = int(milk / 50)

if (beans / 15) > 1.0:
    qty_possible_beans = math.ceil(int(beans / 15))
else:
    qty_possible_beans = int(beans / 15)

qty_possible = min(qty_possible_water, qty_possible_milk, qty_possible_beans)

rest_cup = qty_possible - qty_cup_coffee

if (water > qty_water) and (milk > qty_milk) and (beans > qty_beans):
    print("Yes, I can make that amount of coffee (and even", rest_cup ,"more than that)")
    # print("For", qty_cup_coffee, "cups of coffee you will need:")
    # print(qty_water, "ml of water")
    # print(qty_milk, "ml of milk")
    # print(qty_beans, "g of coffee beans")

else:
    print(qty_possible_beans, qty_possible_milk, qty_possible_water)

    print("No, I can make only", qty_possible, "cup(s) of coffee")


print("Starting to make a coffee")
print("Grinding coffee beans")
t.sleep(2)
print("Boiling water")
t.sleep(2)
print("Mixing boiled water with crushed coffee beans")
t.sleep(2)
print("Pouring coffee into the cup")
t.sleep(2)
print("Pouring some milk into the cup")
t.sleep(2)
print("Coffee is ready!")
"""
