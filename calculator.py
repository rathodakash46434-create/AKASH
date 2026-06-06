"""
Simple Calculator Application
A basic calculator that performs basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():
    """Main calculator function"""
    print("=" * 50)
    print("        SIMPLE CALCULATOR APPLICATION")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
            
            except ValueError:
                print("\nInvalid input! Please enter valid numbers.")
        else:
            print("\nInvalid choice! Please select a valid operation.")


if __name__ == "__main__":
    calculator()
