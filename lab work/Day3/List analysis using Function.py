def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers)

numbers = []

print("Enter 10 integers:")
for i in range(10):
    value = int(input(f"Enter integer {i + 1}: "))
    numbers.append(value)

print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
print("Average:", find_average(numbers))