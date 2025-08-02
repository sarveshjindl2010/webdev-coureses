num = int(input("Enter a number to check :"))

if num > 7:
    print("The number is greater than 7")
    if num%2==0:
        print("The number is even too")
    else:
        print("The number is odd")
else:
    print("Number is less than 7")        