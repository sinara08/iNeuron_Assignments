#Write a Python program to print &quot;Hello Python&quot;?

print("Hello Python")
print("====================================")
#Write a Python program to do arithmetical operations addition and division.?

i = 50
j = 10
print("Addition of two numbers",i+j)
print("Division of two numbers",i/j)
print("====================================")

#Write a Python program to find the area of a triangle?
base = 5
h = 3
area = (base * h)/2
print("Area of a triangle when base = {} and height = {} is {}".format(base, h, area))
print("====================================")

#Write a Python program to swap two variables?

a = 10
b = 20
print("Before swapping a={} and b = {}".format(a,b))
temp = a
a = b
b = temp
print("After swapping a={} and b = {}".format(a,b))
print("====================================")

#Write a Python program to generate a random number?
import random

print("Random number in the range of 1 to 100 ", random.randint(1,100))
