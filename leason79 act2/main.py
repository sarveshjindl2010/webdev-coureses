def OnTime(n):
    iteration = 0
    for i in range(1,n+1):
        iteration+=3
    print("when n is ",n," Iteration = ",iteration)

OnTime(20)
OnTime(50)
OnTime(90)

print("\n with every 'n' the time taken and iterations will increase linearly")
#order to complaexity