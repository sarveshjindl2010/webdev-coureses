fn = open('how.txt', 'r')
fn1 = open('how1.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
fn1.close()
fn1 = open('how.txt', 'r')
cont1 = fn1.read()
fn.close()
fn1.close()