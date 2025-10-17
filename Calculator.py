"""
Calculator CLI Application
A command-line calculator supporting basic arithmetic operations.
"""

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
        return "Error: Division by zero is not allowed"
    return x / y


def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("     WELCOME TO CLI CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add       (+)")
    print("2. Subtract  (-)")
    print("3. Multiply  (*)")
    print("4. Divide    (/)")
    print("5. Exit")
    print("="*40)


def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return None, None


def main():
    """Main calculator loop"""
    print("\nWelcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using Calculator CLI. Goodbye!\n")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                print(f"\n{num1} + {num2} = {add(num1, num2)}\n")
            elif choice == '2':
                print(f"\n{num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == '3':
                print(f"\n{num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}\n")
        else:
            print("\nInvalid choice! Please select a valid operation (1-5).\n")


if __name__ == "__main__":
    main()