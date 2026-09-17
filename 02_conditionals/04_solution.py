# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input("Enter the color of the fruit: ")

if fruit == "Banana":
    if color.lower() == "green":
        print("Unripe")
    elif color.lower() == "yellow":
        print("Ripe")
    elif color.lower() == "brown":
        print("Overripe")
    else:
        print("Unknown color")
else :
    print("Fruit information is not available")