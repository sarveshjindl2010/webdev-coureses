def setOrNot(number, n):
    mask = 1 # Assuming you want to check if the bit is set or not
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n-1)):
            print("Set")
        else:
            print("NOT SET")
number = int(input("Enter your number: "))
n = int(input("Enter the bit poistion: "))
setOrNot(number, n)