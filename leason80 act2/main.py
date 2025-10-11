def sum(n):
    return n*(n+1)/2
#Space compexity: O(1),Auxilary space = O(1)
#linear space:
def arraysum(a):
    sum=0
    for i in a:
        sum+=i

    return(sum)
a = [12, 3, 4, 51]
arraysum(a)
#with the size of the array, the space also required increase
#space complexity: O(n),Auxilary spcae = O(1)
def sum(n):
    if(n<=0):
        return
    return n+ sum(n-1)