# Create a list
tea = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

# Print list
print(tea)

# Indexing (0-based)
tea[0]          # First item
tea[-1]         # Last item

# Slicing
tea[1:3]        # Index 1 to 2
tea[:2]         # Start to index 1
tea[2:]         # Index 2 to end
tea[::2]        # Every 2nd item

# Change an item
tea[3] = "Herbal Tea"

# Replace multiple items
tea[1:3] = ["Green Tea", "Masala Tea"]

# Add item at end
tea.append("Lemon Tea")

# Remove last item
tea.pop()

# Remove specific item
tea.remove("Green Tea")

# Insert at a position
tea.insert(1, "Green Tea")

# Copy list (new/different list)
tea_copy = tea.copy()

# Direct assignment = same reference
tea_copy = tea

# Loop through list
for t in tea:
    print(t)

# Conditional + membership
if "Oolong Tea" in tea:
    print("I have Oolong Tea")

# List comprehension
squares = [x * x for x in range(10)]

# Cube using list comprehension
cubes = [x * x * x for x in range(5)]

# range(10) → 0 to 9
numbers = range(10)

# range values in a list
numbers = list(range(10))

# Empty slice
tea[1:1]       # []

# Delete items using slicing
del tea[1:3]

# Add/insert multiple items using slicing
tea[1:1] = ["Green Tea", "Masala Tea"]

# Print items on same line
for t in tea:
    print(t, end="-")