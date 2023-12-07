"""Name: Roy Mor Yosef
Date: 7.12.23"""


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        return "Error: Division by zero"
    return x / y


def power(x, y):
    """Power Function"""
    return x ** y


def get_number(input_prompt):
    """Function to get valid number input"""
    while True:
        try:
            number = float(input(input_prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculator():
    """Main function to run the calculator"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            elif choice == '5':
                print(f"{num1} ** {num2} = {power(num1, num2)}")

            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to do another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    calculator()
