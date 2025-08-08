num = int(input('Enter number to be checked : '))

prime = True
if num  > 1:
    for i in range(2, num):
        if (num% i == 0):
            prme = False
            break
if prime==True:
    print(num, "is is a prime number")
else:
    print(num, "is not a prime number")          