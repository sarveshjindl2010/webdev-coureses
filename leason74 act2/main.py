new_file = open('yo.txt', 'x')
new_file.close()
import os
print("Checking if my_file exists or not ...")
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print('the file dose not exist')
my_file = open("my_file.txt", 'w')
my_file.write("Hi i am Penguin of 7 yrs old")
my_file.close()