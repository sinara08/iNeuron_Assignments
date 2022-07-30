#Write a Python Program to Check if a Number is Positive, Negative or Zero?
numb = int(input("Enter a valid number: "))

if numb > 0:
    print('Entered number {} is Positive'.format(numb))
elif numb < 0:
    print('Entered number {} is Negative'.format(numb))
elif numb == 0:
    print('Entered number {} is zero'.format(numb))
else:
    print('Entered number {} is not valid'.format(numb))