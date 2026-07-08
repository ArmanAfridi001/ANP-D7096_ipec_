def check_password(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_length = len(password) >= 8

    if has_length and has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


password = input("Enter your password: ")
print(check_password(password))