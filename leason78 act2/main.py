def fun1(n):
    return n*(n+1)/2
print(fun1(5))
#here we take the value of n = 5, so the equation will go as 5*(5+1)/2 = 15
#contant time complexity becasue increase in input, the time does not change
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
#here, we take that sum = 0 and for the i value in the range it willl increase by 1 untill it reaches n+1 where sum will be += i
#time compexity n because when we increase input, the time is increased by same value
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
        return sum
# the time complexity is n*i because the outer loop is running n time and the inner loop is running  i times