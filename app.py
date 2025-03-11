num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Error: Division by zero"
}

result = operations.get(operation, "Invalid operation")
print(result if isinstance(result, str) else f"{num1} {operation} {num2} = {result}")

input("Press Enter to exit.")
