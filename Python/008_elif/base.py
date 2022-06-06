a = int(input("Enter first number:"))
b = input("Enter an operator:")
c = int(input("Enter second number:"))
d = a + c
e = a - c
f = a * c
g = a/c
if b == '+':
    print(str(a) + "+" + str(c) + "=" + str(d))
elif b == '-':
    print(str(a) + '-' + str(c) + '=' + str(e))
elif b == '*':
    print(str(a) + '*' + str(c) + '=' + str(f))
elif b == '/':
    print(str(a) + '+' + str(c) + '=' + str(g))
else:
    print("Error")