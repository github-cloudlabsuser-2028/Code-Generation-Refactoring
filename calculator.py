class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

def main():
    calculator = SimpleCalculator()
    operation = input("Enter operation (add, subtract, multiply, divide, factorial): ").strip().lower()
    if operation == "factorial":
        n = int(input("Enter a number: "))
        print(f"Factorial: {calculator.factorial(n)}")
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if operation == "add":
            print(f"Addition: {calculator.add(a, b)}")
        elif operation == "subtract":
            print(f"Subtraction: {calculator.subtract(a, b)}")
        elif operation == "multiply":
            print(f"Multiplication: {calculator.multiply(a, b)}")
        elif operation == "divide":
            print(f"Division: {calculator.divide(a, b)}")
        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()