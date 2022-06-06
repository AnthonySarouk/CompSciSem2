import random
restaurants = ["Chuck E. Cheese", "Kitchen Nightmares", "Sakura" ,"Ratatouille"]
menu = ["Chicken/Soup/Noodles", "Pizza/Bread/Soda", "Toast/Eggs/Milk", "Spaghetti/Ice cream/Steak"]
x = random.randrange(3)
if x == 0:
    print(restaurants[0])
    print(menu[0])
    a = input("Choose an item from the menu:")
    if a == "Chicken" or a == "Soup" or a == "Noodles":
      print("Enjoy your" + a)
    else:
      print("Not within menu")
elif x == 1:
    print(restaurants[1])
    print(menu[1])
    a = input("Choose an item from the menu:")
    if a == "Pizza" or a == "Bread" or a == "Soda":
        print("Enjoy your" + a)
    else:
        print("Not within menu")
elif x == 2:
    print(restaurants[2])
    print(menu[2])
    a = input("Choose an item from the menu:")
    if a == "Toast" or a == "Eggs" or a == "Milk":
        print("Enjoy your" + a)
    else:
        print("Not within menu")
elif x == 3:
    print(restaurants[3])
    print(menu[3])
    a = input("Choose an item from the menu:")
    if a == "Spaghetti" or a == "Ice Cream" or a == "Steak":
        print("Enjoy your" + a)
    else:
        print("Not within menu")


    