#file handling
import os
try:
    with open("test.txt","w") as file1:
        file1.write("Testing python file handling")
except IOError:
    print("Error: could not create file " + file1)

with open("test.txt","a") as file1:
    file1.write("Adding python file handling")

with open("test.txt") as file1:
    read_content = file1.read()
    print(read_content)

# os.mkdir("testfile")
os.getcwd()
os.chdir("/home/dev/PycharmProjects/pythonProject/testfile")
try:
    with open("test3.txt","w") as file3:
        file3.write("Testing python file handling")
except IOError:
    print("Error: could not create file test3.txt")


with open("test.txt","a") as file1:
    file1.write("Adding more python file handling")

with open("test.txt") as file1:
    read_content = file1.read()
    print(read_content)