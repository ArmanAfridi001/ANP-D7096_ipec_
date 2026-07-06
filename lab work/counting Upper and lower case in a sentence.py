sentence = input("Enter a sentence: ")

upper_count = 0
lower_count = 0

for ch in sentence:
    if 'A' <= ch <= 'Z':
        upper_count += 1
    elif 'a' <= ch <= 'z':
        lower_count += 1

print("Uppercase characters:", upper_count)
print("Lowercase characters:", lower_count)