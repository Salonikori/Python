# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter the species of your pet: ").lower()
age = int(input("Enter the age: "))

if species == "dog":
    if age < 2:
        recommendation = "Puppy Food"
    else:
        recommendation = "Adult Dog Food"
elif species == "cat":
    if age <= 5:
        recommendation = "Junior cat food"
    else:
        recommendation = "Senior cat food"
else :
    recommendation ="Not available"

print(f"Recommendation for your {species} of {age} is {recommendation}")