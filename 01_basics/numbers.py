# Numbers
x = 10
y = 3
x + y
x - y
x * y
x / y

# Floor division
x // y 

# Remainder
x % y

# Power
x ** y


# Type conversion
int(2.5)          # 2
float(10)         # 10.0


# Comparison
x > y
x < y
x >= y
x <= y
x == y
x != y            # Returns True/False


# Logical operators
x > 5 and y < 5   # Both must be True
x > 5 or y > 5    # At least one must be True


# Boolean
a = True
b = False

True == 1         # True
False == 0        # True


# Tuple
values = (x, y, 10)

# Multiple values
x, y, z = 2, 3, 4


# Math library
import math

math.floor(3.5)   # 3
math.floor(-3.5)  # -4
math.trunc(2.8)   # 2
math.trunc(-2.8)  # -2


# Complex number
num = 2 + 1j


# Binary
bin(64)

# Octal
oct(64)

# Hexadecimal
hex(64)


# Bitwise
x << 2            # Left shift
x >> 2            # Right shift
x & 2             # Bitwise AND
x | 2             # Bitwise OR


# Random numbers
import random

random.randint(1, 100)     # Random integer

tea = ["Black", "Green", "White"]

random.choice(tea)         # Random element
random.shuffle(tea)        # Shuffle list


# Decimal for precise decimal calculations
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.1")

a + b


# Fraction
from fractions import Fraction

f = Fraction(2, 7)


# Set
set1 = {1, 2, 3, 4}
set2 = {1, 3, 5}

# Intersection
set1 & set2

# Union
set1 | set2

# Difference
set1 - set2

# Empty set
empty = set()              # NOT {}


# Set membership
2 in set1


# Boolean type
type(True)                 # bool
type(10)                   # int
type(10.5)                 # float