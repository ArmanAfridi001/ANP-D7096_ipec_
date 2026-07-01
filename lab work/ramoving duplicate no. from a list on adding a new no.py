# Create a list of 20 numbers
numbers = []

print("Enter 20 numbers:")
for i in range(20):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Ask the user for the number to remove
target = int(input("\nEnter a number to remove from the list: "))

# Remove all occurrences of the number
while target in numbers:
    numbers.remove(target)

print("\nUpdated List:", numbers)