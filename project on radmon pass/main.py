import random 
l = ['1', '3', '5']
password = []
for i in range(5):
    password.append(random.choice(l))
print(password)