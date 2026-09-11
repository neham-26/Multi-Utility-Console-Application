"""Number utilities: digits, swap, sign, even/odd."""

from services.input_utils import read_int, read_float


class NumberUtility:
    def calculate_digit_sum(self, number):
        n = abs(int(number))
        total = 0
        if n == 0:
            return 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    def swap_values(self, first, second):
        return second, first

    def identify_sign(self, number):
        if number > 0:
            return "Positive"
        if number < 0:
            return "Negative"
        return "Zero"

    def even_or_odd(self, number):
        if number % 2 == 0:
            return "Even"
        return "Odd"


def show_number_menu():
    print()
    print("=" * 40)
    print("            NUMBER UTILITIES")
    print("=" * 40)
    print("1. Calculate Sum of Digits")
    print("2. Swap Two Values")
    print("3. Check Positive, Negative, or Zero")
    print("4. Check Even or Odd")
    print("5. Return to Main Menu")
    print("=" * 40)


def run_number_module():
    utility = NumberUtility()

    while True:
        show_number_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            number = read_int("Enter an integer: ")
            result = utility.calculate_digit_sum(number)
            print(f"Sum of digits of {number} = {result}")
        elif choice == "2":
            a = read_float("Enter first value: ")
            b = read_float("Enter second value: ")
            print(f"Before swap: first = {a}, second = {b}")
            a, b = utility.swap_values(a, b)
            print(f"After swap:  first = {a}, second = {b}")
        elif choice == "3":
            number = read_float("Enter a number: ")
            print(f"{number} is {utility.identify_sign(number)}")
        elif choice == "4":
            number = read_int("Enter an integer: ")
            print(f"{number} is {utility.even_or_odd(number)}")
        elif choice == "5":
            return
        else:
            print("Invalid option. Choose 1 to 5.")