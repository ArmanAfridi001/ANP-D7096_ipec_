sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)

most_frequent_word = ""
max_count = 0
for word, count in frequency.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print("Most frequent word:", most_frequent_word)

print("Words in alphabetical order:")
for word in sorted(frequency):
    print(word)