import re

def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1

    # Check uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1

    # Check lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1

    # Check number
    if re.search(r'[0-9]', password):
        strength += 1

    # Check special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    # Result
    if strength <= 2:
        return "Weak Password"
    elif strength == 3 or strength == 4:
        return "Medium Password"
    else:
        return "Strong Password"

# Asking user to enter password
password = input("Enter your password: ")
result = check_password_strength(password)
print(f"Password Strength: {result}")

