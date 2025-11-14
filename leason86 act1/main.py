def power2(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0
n = int(input("Enter a number: "))
if power2(n):
    print("\n Its is power of 2 ")
else:
    print("\n It isn't a power of 2")