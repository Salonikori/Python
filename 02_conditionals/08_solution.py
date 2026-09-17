# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")
char = len(password)
if char < 6:
    strength = "Weak"
elif char < 11:
    strength = "Medium"
else:
    strength = "Strong"

print("Passwor is",strength)