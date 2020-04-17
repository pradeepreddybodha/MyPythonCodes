
file = open("text.txt", 'r')
print(file.tell())
print(file.read())
print(file.tell())
file.seek(5)
for i in file:
    print(i, end="")
file.close()
file = open("text.txt", 'a')
file.write("\nWelcome to the world of Python\nStart Learning Python")
print(file.close())
file = open("text.txt", 'r')
print(file.read())

