# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

print("Menu : \n Small \n Medium \n Large \n")
coffee = input("Enter your order: ").lower()

print("\nExtra shot: Espresso")
extra = input("Yes or No").lower() == "yes"

if extra:
    order = coffee + "coffee with an extra shot"
else:
    order = coffee + " coffee without an extra shot"

print(f"Your order is {order}")