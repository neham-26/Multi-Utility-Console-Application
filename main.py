"""
Entry point of the Multi-Utility Console Application.
Only navigation lives here. Business logic is in services/.
"""

from services.student_service import run_student_module
from services.calculator_service import run_calculator_module
from services.conversion_service import run_conversion_module
from services.geometry_service import run_geometry_module
from services.salary_service import run_salary_module
from services.marks_service import run_marks_module
from services.billing_service import run_billing_module
from services.number_service import run_number_module


def show_main_menu():
    print()
    print("=" * 44)
    print("      MULTI-UTILITY CONSOLE APPLICATION")
    print("=" * 44)
    print("1. Student Profile Management")
    print("2. Calculator Operations")
    print("3. Unit Converter")
    print("4. Geometry Calculator")
    print("5. Salary Calculator")
    print("6. Marks Analyzer")
    print("7. Product Billing System")
    print("8. Number Utilities")
    print("9. Exit")
    print("=" * 44)


def main():
    while True:
        show_main_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            run_student_module()

        elif choice == "2":
            run_calculator_module()

        elif choice == "3":
            run_conversion_module()

        elif choice == "4":
            run_geometry_module()

        elif choice == "5":
            run_salary_module()

        elif choice == "6":
            run_marks_module()

        elif choice == "7":
            run_billing_module()

        elif choice == "8":
            run_number_module()

        elif choice == "9":
            print("Thank you for using the application. Goodbye!")
            break

        else:
            print("Invalid menu option. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()