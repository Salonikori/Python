# 4. Reverse a String
# Problem: Reverse a string using a loop.

string = input("Enter a string: ")
reverse_string = ""

for char in string:
    reverse_string= char + reverse_string 

print(reverse_string)