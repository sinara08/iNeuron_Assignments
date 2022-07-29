import math

#solution is (-b+sqrt(b2 - 4ac))/2a, (-b-sqrt(b2 - 4ac))/2a
a = int(input("Enter the value of a( a should not be 0): "))
b = int(input("Enter the value of b( b should not be 0): "))
c = int(input("Enter the value of c( c should not be 0): "))
x = []

x1 = (-b + math.sqrt((b*b) - (4*a*c)))/(2*a)
x2 = (-b - math.sqrt((b*b) - (4*a*c)))/(2*a)
x.append(x1)
x.append(x2)
print("Final result of quadratic equation for the given inputs are: {}:".format(x))
