# calculator_service.py
def run_calculator_module():
    print("Calculator module under construction.")

from services.input_utils import read_float 


class Calculator:
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def add(self):
        return self.__number1 + self.__number2

    def subtract(self):
        return self.__number1 - self.__number2  

    def multiply(self):
        return self.__number1 * self.__number2 

    def divide(self):
        if self.__number2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.__number1 / self.__number2

    def modulus(self):
        if self.__number2 == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return self.__number1 % self.__number2

    def power(self):
        return self.__number1 ** self.__number2 

def _show_calculator_menu():
    print("**** Calculator Module ****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Return to Main Menu")

def run_calculator_module():
    while True:
        _show_calculator_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '7':
            return  # Return to the main menu

        n1 = read_float("Enter the first number: ")
        n2 = read_float("Enter the second number: ")

        calculator = Calculator(n1, n2)

        try:
            if choice == '1':
                result = calculator.add()
                symbol = '+'
                print(f"Result: {result}")
            elif choice == '2':
                result = calculator.subtract()
                symbol = '-'
                print(f"Result: {result}")
            elif choice == '3':
                result = calculator.multiply()
                symbol = '*'
                print(f"Result: {result}")
            elif choice == '4':
                result = calculator.divide()
                symbol = '/'    
                print(f"Result: {result}")
            elif choice == '5':
                result = calculator.modulus()
                symbol = '%'
                print(f"Result: {result}")
            elif choice == '6':
                result = calculator.power()
                symbol = '**'
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please choose a number from 1 to 7.")
        except ZeroDivisionError as error:
            print(f"Error: {error}")