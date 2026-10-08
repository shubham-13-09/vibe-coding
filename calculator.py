# Simple calculator program
# This script takes two numbers from the user and performs basic arithmetic operations.

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the required operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division carefully to avoid dividing by zero
if num2 == 0:
    division_result = "Cannot divide by zero"
else:
    division_result = num1 / num2

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
