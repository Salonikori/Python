# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = int(input("Enter the value of n: "))

for i in range(1,11):
    if i==5:
        continue
    print(f"{n} x {i} = ",n*i)