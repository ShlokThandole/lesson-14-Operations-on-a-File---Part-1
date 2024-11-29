file = open('file for file handling in python.txt', 'r')
print("reading firdt line...............")
print(file.readline())
file.close()

file = open('file for file handling in python.txt', 'r')
print("read so many lines.............")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('file for file handling in python.txt', 'r')
print("looping through the lines..........")
for smite in file:
    print(smite)
file.close()