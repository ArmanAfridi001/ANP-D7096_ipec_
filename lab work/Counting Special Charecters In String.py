text = input("Enter a string: ")

special_count = 0

for ch in text:
    if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
        special_count += 1

print("Number of special characters:", special_count)