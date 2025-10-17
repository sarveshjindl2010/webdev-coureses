def print_factors(number):
    print('The factors of', number,"are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input("Enter ypur number to find its factor's:"))
print_factors(number)