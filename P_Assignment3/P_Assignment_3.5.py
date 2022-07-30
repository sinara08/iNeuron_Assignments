#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
numb = 1
lst=[]

while numb <= 10000:
    flag = 1
    rslt = numb % 2

    if rslt != 0:
        if numb > 8:
            for i in range(3, 9, 2):
                if numb % i == 0:
                    flag = 0
                    break
            if flag == 1:
                lst.append(numb)

        else:
            if numb != 1:
                lst.append(numb)
    elif numb == 2:
        lst.append(numb)
    numb += 1

print("Prime numbers are: ",lst)