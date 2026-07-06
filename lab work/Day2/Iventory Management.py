inventory = {
    'Laptop': 15,
    'Mouse': 40,
    'Keyboard': 25,
    'Monitor': 10
}

print("Current inventory:")
for product, stock in inventory.items():
    print(product, "->", stock)

product = input("\nEnter a new product name to add: ")
stock = int(input("Enter stock quantity: "))
inventory[product] = stock

print("\nAfter adding new product:")
for product, stock in inventory.items():
    print(product, "->", stock)

product = input("\nEnter product name to update stock: ")
if product in inventory:
    stock = int(input("Enter new stock quantity: "))
    inventory[product] = stock
    print("Stock updated.")
else:
    print("Product not found.")

product = input("\nEnter product name to remove: ")
if product in inventory:
    del inventory[product]
    print("Product removed.")
else:
    print("Product not found.")

print("\nProducts with stock less than 20:")
for product, stock in inventory.items():
    if stock < 20:
        print(product, "->", stock)

total_stock = 0
for stock in inventory.values():
    total_stock += stock

print("\nTotal number of items available:", total_stock)