# Problem Statement
# An airline calculates ticket fare using:
# Base Fare = ₹5000
# Additional Charges:
# •
# Business Class → +₹3000
# •
# Window Seat → +₹500
# •
# Weekend Travel → +₹1000
# Discounts:
# •
# Age below 12 → 50%
# •
# Age above 60 → 20%
# Calculate the final ticket fare.
# Sample Input
# Enter Passenger Age: 65 Business Class (Y/N): Y Window Seat (Y/N): Y Weekend Travel (Y/N): Y
# Sample Output
# Base Fare: ₹5000 Additional Charges: ₹4500 Senior Citizen Discount: 20% Final Ticket Fare: ₹7600.0
# e fare
# fare = 5000

age = int(input("Enter Passenger Age: "))
business = input("Business Class (Y/N): ").upper()
window = input("Window Seat (Y/N): ").upper()
weekend = input("Weekend Travel (Y/N): ").upper()

# Calculate additional charges
additional = 0

if business == "Y":
    additional += 3000

if window == "Y":
    additional += 500

if weekend == "Y":
    additional += 1000

# Total before discount
total_fare = fare + additional

# Apply discount
if age < 12:
    discount = 50
    final_fare = total_fare * 0.50
elif age > 60:
    discount = 20
    final_fare = total_fare * 0.80
else:
    discount = 0
    final_fare = total_fare

# Output
print("Base Fare: ₹", fare)
print("Additional Charges: ₹", additional)

if discount == 50:
    print("Child Discount: 50%")
elif discount == 20:
    print("Senior Citizen Discount: 20%")
else:
    print("No Discount")

print("Final Ticket Fare: ₹", final_fare)