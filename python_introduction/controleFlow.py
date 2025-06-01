purchase_amount = float(input("Enter your purchase amount: "))  # Fixed input

if purchase_amount >= 1000:
    discount = 0.1  # 10% discount
elif purchase_amount >= 500:
    discount = 0.05  # 5% discount
else:
    discount = 0  # No discount
age = 32
message = "eligable" if age >=18 else "noteligabel"

print(message)

final_price = purchase_amount * (1 - discount)  # Fixed variable name
print("Final price after discount: $" + str(final_price))  # Cleaner output
