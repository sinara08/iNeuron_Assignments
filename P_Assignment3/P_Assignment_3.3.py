#Write a Python Program to Check Leap Year?

yr = int(input("Enter a valid year: "))

rslt = yr % 4
if rslt == 0:
    print('Entered year {} is a Leap year'.format(yr))
else:
    print('Entered year {} is not a Leap year'.format(yr))