# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

string = input("Enter a string: ")

for char in string:
    if string.count(char) == 1:
        print(char)
        break

   