def primeSeive(n):
    prime = [True for i in range(n + 1)]
    CurrentNumber = 2
    while(CurrentNumber * CurrentNumber <= n):
        if (prime[CurrentNumber] == True):
            for i in range(CurrentNumber ** 2, n + 1, CurrentNumber):
                prime[i] = False
        CurrentNumber +=1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p)
n = int(input("Enter number to find all prime numbers less than the number :"))
primeSeive(n)
print("Following are the prime numbers smaller")
print ("than or equal to")