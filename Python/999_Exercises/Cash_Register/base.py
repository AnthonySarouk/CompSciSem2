x = int(input("How many items are you purchasing?"))
total = 0
for x in range(0,x):
    b = input("What item are you purchasing?")
    c = int(input("How much does the item cost?"))
    total += c
    print("Thank you for puchasing" + b)
    print("________________________________")
print("Your total is: " + str(total))