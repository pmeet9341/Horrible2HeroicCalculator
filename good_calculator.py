def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

def calculate(x, y, op):
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations[op](x, y) if op in operations else "Invalid operation"

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    print(f"Result: {calculate(x, y, op)}")

if __name__ == "__main__":
    main()
