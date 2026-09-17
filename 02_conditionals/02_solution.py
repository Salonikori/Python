# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
day = input("Enter the day: ")

# if age < 18:
#     price = 8
# else:
#     price = 12

price = 12 if age >= 18 else 8
if day == "Wednesday" or day == "wednesday" :
    # price = price-2
    price -= 2

print(f"Your movie tickets are of {price} dollars")