# Create a tuple
tea_types = ("Black Tea", "Green Tea", "Oolong Tea")

# Tuple can contain numbers too
numbers = (1, 2, 3)

# Access using index
tea_types[0]

# Negative indexing
tea_types[-1]

# Slicing
tea_types[0:2]

# Slicing with step
tea_types[::2]

# Tuple is IMMUTABLE
# Cannot change an existing value
# tea_types[0] = "Lemon Tea"   # TypeError

# Length of tuple
len(tea_types)

# Add more values by creating a NEW tuple
more_tea = ("Herbal Tea", "Earl Grey")

all_tea = tea_types + more_tea

# Membership check
if "Green Tea" in all_tea:
    print("I have Green Tea")

# Count duplicate values
tea = ("Herbal Tea", "Earl Grey", "Herbal Tea")
tea.count("Herbal Tea")

# Find position
tea.index("Earl Grey")

# Check type
type(tea_types)       # <class 'tuple'>

# Tuple unpacking
tea_types = ("Black Tea", "Green Tea", "Oolong Tea")

black, green, oolong = tea_types

print(black)
print(green)
print(oolong)

# Number of variables must match number of values
# black, green = tea_types   # ValueError

# Nested tuple
nested = (
    "Black Tea",
    ("Green Tea", "Oolong Tea"),
    "Herbal Tea"
)

# Access nested tuple
nested[1]

# Access value inside nested tuple
nested[1][0]

# Tuples can contain different data types
data = ("Tea", 10, 2.5, True)

# Database commonly returns tuples
# Example:
result = ("Saloni", 20, "Mumbai")

# Tuple unpacking from database result
name, age, city = result