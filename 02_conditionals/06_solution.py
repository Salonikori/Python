# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter distance: "))

if distance < 3:
    mode = "Walk"
elif distance < 16:
    mode = "Bike"
else:
    mode = "Car"

print("Your mode of transportation is", mode)