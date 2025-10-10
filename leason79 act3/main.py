def test(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            iteration+=5
        print("")
    print("\n when n is",n,"iteration =",iteration)
test(7)
test(8)
test(9)

print("\n with every 'n' the time taken = n*2")
print("(n*2)")