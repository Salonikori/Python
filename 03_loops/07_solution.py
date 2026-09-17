# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number between 1 to 10: "))
    if(0<number<11):
        print("Thanks")
        break
    print("Incorrect, Retry")