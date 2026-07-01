# Create a list of 10 elements
numbers = []

print("Enter 10 elements:")
for i in range(10):
    num = int(input(f"Element {i + 1}: "))
    numbers.append(num)

# Display the original list
print("\nOriginal List:", numbers)

index = int(input("Enter the index to remove (0 to 9): "))

# Check if the index is valid
if 0 <= index < len(numbers):
    removed = numbers.pop(index)
    print("Removed Element:", removed)
    print("Updated List:", numbers)
else:
    print("Invalid index!")