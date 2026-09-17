# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter weather: ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"
else:
    activity = "Unknown weather"

print("Activity is ",activity)