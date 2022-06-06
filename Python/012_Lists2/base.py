import random
a = int(input("How many random numbers would you like to print?"))
thislist = []
for b in range(0,a):
    x = (random.randrange(1,10))
    thislist.append(x)
print("Your numbers are :" + str(thislist))

