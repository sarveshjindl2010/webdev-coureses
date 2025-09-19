file1 = open('File.txt',  'r')
file2 = open('fileUpdated.txt', 'w')
for line in file1.readlines():
    print(line)
    file2.write(line)
file2.close()
file1.close()    