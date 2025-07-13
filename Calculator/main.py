import os
import math

class Calculator:
    def __init__(self):
        self.history = []
        self.operations = {
            '1': ('Addition', '+', self.add),
            '2': ('Subtraction', '-', self.subtract),
            '3': ('Multiplication', '*', self.multiply),
            '4': ('Division', '/', self.divide),
            '5': ('Power', '^', self.power),
            '6': ('Modulo', '%', self.modulo),
            '7': ('Square Root', '√', self.square_root),
            '8': ('Percentage', '%', self.percentage)
        }

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self):
        """Display calculator header."""
        print("=" * 50)
        print("🔢 SIMPLE CALCULATOR 🔢")
        print("=" * 50)
        print()

    def display_menu(self):
        """Display operation menu."""
        print("📋 AVAILABLE OPERATIONS:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Power (^)")
        print("6. Modulo (%)")
        print("7. Square Root (√)")
        print("8. Percentage (%)")
        print("9. View History")
        print("10. Clear History")
        print("11. Exit")
        print("-" * 40)

    def get_number(self, prompt):
        """Get a valid number from user input."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    def get_operation(self):
        """Get operation choice from user."""
        while True:
            choice = input("Enter operation choice (1-11): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                return choice
            elif choice == '9':
                return 'history'
            elif choice == '10':
                return 'clear_history'
            elif choice == '11':
                return 'exit'
            else:
                print("❌ Invalid choice! Please enter a number between 1-11.")

    def add(self, a, b):
        """Addition operation."""
        return a + b

    def subtract(self, a, b):
        """Subtraction operation."""
        return a - b

    def multiply(self, a, b):
        """Multiplication operation."""
        return a * b

    def divide(self, a, b):
        """Division operation."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def power(self, a, b):
        """Power operation."""
        return a ** b

    def modulo(self, a, b):
        """Modulo operation."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        return a % b

    def square_root(self, a, b=None):
        """Square root operation (only uses first number)."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)

    def percentage(self, a, b):
        """Percentage operation (a% of b)."""
        return (a / 100) * b

    def format_number(self, num):
        """Format number for display."""
        if num == int(num):
            return str(int(num))
        else:
            return f"{num:.6f}".rstrip('0').rstrip('.')

    def save_to_history(self, operation, num1, num2, result):
        """Save calculation to history."""
        if operation == '7':  # Square root
            expression = f"√{self.format_number(num1)} = {self.format_number(result)}"
        else:
            op_symbol = self.operations[operation][1]
            expression = f"{self.format_number(num1)} {op_symbol} {self.format_number(num2)} = {self.format_number(result)}"
        
        self.history.append(expression)

    def display_history(self):
        """Display calculation history."""
        if not self.history:
            print("📝 No calculations in history yet!")
            return
        
        print("📝 CALCULATION HISTORY:")
        print("-" * 30)
        for i, calculation in enumerate(self.history, 1):
            print(f"{i}. {calculation}")
        print("-" * 30)

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        print("🗑️ History cleared!")

    def perform_calculation(self, operation):
        """Perform the selected calculation."""
        op_name, op_symbol, op_function = self.operations[operation]
        
        print(f"\n🔢 {op_name} Operation")
        print("-" * 25)
        
        # Get first number
        num1 = self.get_number("Enter first number: ")
        
        # For square root, we only need one number
        if operation == '7':
            try:
                result = op_function(num1)
                print(f"\n✅ RESULT:")
                print(f"√{self.format_number(num1)} = {self.format_number(result)}")
                self.save_to_history(operation, num1, None, result)
            except ValueError as e:
                print(f"❌ Error: {e}")
        else:
            # Get second number for other operations
            num2 = self.get_number("Enter second number: ")
            
            try:
                result = op_function(num1, num2)
                print(f"\n✅ RESULT:")
                print(f"{self.format_number(num1)} {op_symbol} {self.format_number(num2)} = {self.format_number(result)}")
                self.save_to_history(operation, num1, num2, result)
            except ValueError as e:
                print(f"❌ Error: {e}")
            except ZeroDivisionError:
                print("❌ Error: Cannot divide by zero!")

    def run(self):
        """Main calculator loop."""
        print("Welcome to the Simple Calculator! 🎉")
        print("Perform basic arithmetic operations with ease.")
        print()
        
        while True:
            self.display_menu()
            
            choice = self.get_operation()
            
            if choice == 'exit':
                break
            elif choice == 'history':
                self.display_history()
            elif choice == 'clear_history':
                self.clear_history()
            else:
                self.perform_calculation(choice)
            
            # Ask if user wants to continue
            print("\n" + "=" * 50)
            continue_calc = input("Press Enter to continue or 'q' to quit: ").strip().lower()
            if continue_calc == 'q':
                break
            
            self.clear_screen()
            self.display_header()
        
        print("\n🎊 Thank you for using the Simple Calculator!")
        if self.history:
            print(f"You performed {len(self.history)} calculation(s) today!")

def main():
    """Main function to start the calculator."""
    calculator = Calculator()
    calculator.clear_screen()
    calculator.display_header()
    calculator.run()

if __name__ == "__main__":
    main()
