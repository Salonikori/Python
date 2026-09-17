# Create string
tea = "Masala Tea"

# First character
tea[0]

# Last character
tea[-1]

# Slicing
tea[0:6]

# Slicing with step
tea[::2]

# Reverse string
tea[::-1]


# Convert to lowercase
tea.lower()

# Convert to uppercase
tea.upper()

# Remove extra spaces
tea.strip()

# Replace text
tea.replace("Masala", "Ginger")


# Split string into list
tea = "Lemon, Ginger, Masala"
tea.split(", ")

# Find position
tea.find("Masala")

# Count occurrences
tea.count("Tea")

# Check if text exists
"Masala" in tea


# String length
len(tea)


# Loop through string
for letter in tea:
    print(letter)


# String formatting
tea_type = "Masala"
quantity = 2

order = "I ordered {} cups of {}".format(quantity, tea_type)
print(order)


# Convert list to string
tea_list = ["Lemon", "Ginger", "Masala"]

tea_string = ", ".join(tea_list)
print(tea_string)


# Escape character
text = "He said \"Masala Tea is awesome\""

# \n → New line
print("Masala\nTea")


# Raw string
path = r"C:\Users\Saloni\Documents"

print(path)


# Check substring
tea = "Masala Tea"

"Masala" in tea       # True
"Coffee" in tea       # False