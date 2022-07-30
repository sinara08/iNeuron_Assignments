#Write a Python Program to Check if a Number is Odd or Even?
numb = int(input("Enter a valid number: "))

rslt = numb % 2
if rslt == 0:
    print('Entered number {} is Even'.format(numb))
else:
    print('Entered number {} is Odd'.format(numb))
