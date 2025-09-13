file = open("file.txt", "r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    counter +=1
print("This is the number of lines in the file")
print(Counter)    