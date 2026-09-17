# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the value of n: "))
total = 0

for num in range(1,n+1):
    if num%2 == 0:
        total = total + num

print("The sum of even numbers is", total)