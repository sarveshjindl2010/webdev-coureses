def fun1(n):
    return n*(n+1)/2
#contant time complexity
print(fun1(5))
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i
#time complexity n
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
        return sum
#time compexity will be n*i