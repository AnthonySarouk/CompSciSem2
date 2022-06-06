x = input("Input First Name: ")
y = input("Input Last Name: ")
a = x[0:len(x)]
b = y[0:len(y)]
i = 0
z = 0
for i in range(0,len(x)):
    m = x[i:i+1]
    print(m)
print()
for z in range(0,len(y)):
    n = y[z:z+1]
    print(n)
