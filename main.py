file = open('file for file handling in python.txt', 'r')
print(file.read())

file.close()
file = open('file for file handling in python.txt', 'r')
print("\n read i parts \n")
print(file.read(6))
file.close()

file = open('file for file handling in python.txt', 'a')
file.write("HI WELCOME TO JUMANJI!!!!!!!!!!")
file.close()