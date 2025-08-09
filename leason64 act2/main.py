def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter a Number:"))

if num < 0:
    print("Sorrry, Factorial dosen't exsit for negeative nmbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))     