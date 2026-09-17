# Create a dictionary
tea = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

# Another way to create dictionary
tea = dict(Masala="Spicy", Ginger="Zesty")

# Access value using key
tea["Masala"]

# Access value using get()
tea.get("Ginger")

# Missing key with get() → None
tea.get("Lemon")

# Change a value
tea["Green"] = "Fresh"

# Add a new key-value pair
tea["Earl Grey"] = "Citrus"

# Remove using pop()
tea.pop("Ginger")

# Remove using del
del tea["Green"]

# Get all keys
tea.keys()

# Get all values
tea.values()

# Get key-value pairs
tea.items()

# Length of dictionary
len(tea)

# Check if key exists
"Masala" in tea

# Loop through keys
for key in tea:
    print(key)

# Loop through keys and values
for key, value in tea.items():
    print(key, value)

# Conditional with dictionary
if "Masala" in tea:
    print("I have Masala Tea")

# Clear dictionary
tea.clear()

# Copy dictionary (new reference)
tea_copy = tea.copy()

# Nested dictionary
tea_shop = {
    "Tea": {
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },
    "Green": {
        "Green Tea": "Fresh",
        "Black Tea": "Strong"
    }
}

# Access nested dictionary
tea_shop["Tea"]

# Access value inside nested dictionary
tea_shop["Tea"]["Ginger"]

# Dictionary comprehension
squares = {x: x*x for x in range(6)}

# Create dictionary from keys with same default value
keys = ["Masala", "Ginger", "Lemon"]

tea_types = dict.fromkeys(keys, "Delicious")

# Dictionary from two lists
keys = ["Masala", "Ginger", "Lemon"]
values = ["Spicy", "Zesty", "Fresh"]

# zip() pairs corresponding values
tea_types = dict(zip(keys, values))