a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
print("Before swapping, the numbers are {} and {}".format(a,b))
a = a + b
b = a - b
a = a - b
print("After swapping, the numbers are {} and {}".format(a,b))

