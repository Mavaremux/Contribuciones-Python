# Advanced Calculator in Python

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def exponent(x, y):
    """Raise x to the power of y"""
    return x ** y

def root(x, y):
    """Calculate the y-th root of x"""
    return x ** (1/y)

def log(x, base):
    """Calculate the logarithm of x with base"""
    import math
    return math.log(x, base)

def sin(x):
    """Calculate the sine of x"""
    import math
    return math.sin(math.radians(x))

def cos(x):
    """Calculate the cosine of x"""
    import math
    return math.cos(math.radians(x))

def tan(x):
    """Calculate the tangent of x"""
    import math
    return math.tan(math.radians(x))

def main():
    print("Advanced Calculator")
    print("------------------")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Root")
        print("7. Logarithm")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Quit")

        choice = input("Enter your choice (1-11): ")

        if choice == "11":
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = exponent(num1, num2)
        elif choice == "6":
            result = root(num1, num2)
        elif choice == "7":
            base = float(input("Enter the base: "))
            result = log(num1, base)
        elif choice == "8":
            result = sin(num1)
        elif choice == "9":
            result = cos(num1)
        elif choice == "10":
            result = tan(num1)
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"\nThe result is: {result:.2f}")

if __name__ == "__main__":
    main()