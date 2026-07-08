def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


text = input("Enter a sentence: ")
print("Total number of vowels:", count_vowels(text))