file = open('abc.txt', 'w')

try:
    file.write("Hello World")
finally:
    file.close()

# Other option:
with open('xyz.txt', 'w') as file2:
    file2.write("Python")