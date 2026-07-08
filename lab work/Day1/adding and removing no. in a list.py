
numbers = []

print("Enter 20 numbers:")
for i in range(20):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Input the new number
new_num = int(input("\nEnter the new number to add: "))

# Remove all duplicates of the new number
while new_num in numbers:
    numbers.remove(new_num)

# Add the new number once
numbers.append(new_num)

print("\nUpdated List:", numbers)