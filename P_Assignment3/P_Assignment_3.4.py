#Write a Python Program to Check Prime Number?
numb = int(input("Enter a valid number: "))

rslt = numb % 2

if rslt == 0 and numb != 2:
    print('Entered number {} is not prime number'.format(numb))
    exit(0)
else:
    if numb > 8:
        for i in range(3, 9, 2):
            if numb % i == 0:
                print('Entered number {} is not prime number'.format(numb))
                exit(0)
        print('Entered number {} is prime number'.format(numb))
    else:
        if numb == 1:
            print('Entered number {} is not a prime number'.format(numb))
        else:
            print('Entered number {} is a prime number'.format(numb))
