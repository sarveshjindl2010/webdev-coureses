number = int(input("Input number:"))
result = 0
temp = number
while temp!=0:
    digit = temp % 10
    result += digit**3
    temp = temp//10
print(result)
if number == result:
    print(number, "is an amstrong number ")
else:
    print(number, "is not an amstrong number")