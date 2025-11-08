def checkIfSame(number1,number2):
    if((number1 ^ number2)!= 0):
        print("number are not same")

    else:
        print("number are equal")

number1 = int(input("Entert the first number: "))
number2 = int(input("Enter the second number: "))
checkIfSame(number1,number2)