with open('his.txt', 'w') as file:
    file.write("Hi i am penguin and I am 7 yrs old")
file.close()
with open('his.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are ....")
    for line in data:
        word = line.split()
        print(word)
file.close()