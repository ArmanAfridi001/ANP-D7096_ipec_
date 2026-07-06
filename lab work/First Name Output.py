name = input("Enter your full name: ")

first_name = ""

for ch in name:
    if ch != ' ':
        first_name += ch
    else:
        break

print("First name:", first_name)