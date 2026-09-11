Multi-Utility Console Application

A Python-based console application that combines multiple utility modules into one menu-driven program. The project follows basic Object-Oriented Programming (OOP), separation of responsibilities, input validation, and a modular folder structure.

Features

The application provides the following modules:

Student Profile Management

Accepts and displays student information.

Calculates performance and placement eligibility.

Calculator Operations

Addition

Subtraction

Multiplication

Division

Modulus

Exponentiation

Handles division/modulus by zero and invalid input.

Unit Converter

Celsius to Fahrenheit

Fahrenheit to Celsius

Minutes to hours and remaining minutes

Days to years, months, and remaining days

Geometry Calculator

Performs the required geometry calculations through a dedicated class/module.

Salary Calculator

Calculates allowance, bonus, gross salary, deduction, and net salary.

Validates salary and percentage inputs.

Displays monetary values with two decimal places.

Marks Analyzer

Accepts marks for five subjects.

Calculates total and average marks.

Finds highest and lowest marks.

Determines pass/fail status and performance level.

Validates marks between 0 and 100.

Product Billing System

Calculates product billing using quantity, unit price, discount, and tax-related operations.

Validates quantity, price, and discount inputs.

Number Utilities

Calculates sum of digits.

Swaps two values.

Checks whether a number is positive, negative, or zero.

Checks whether a number is even or odd.

Project Structure

Day1_Assignment/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── employee.py
│   └── product.py
│
├── services/
│   ├── __init__.py
│   ├── student_service.py
│   ├── calculator_service.py
│   ├── conversion_service.py
│   ├── geometry_service.py
│   ├── salary_service.py
│   ├── marks_service.py
│   ├── billing_service.py
│   └── number_service.py
│
├── screenshots/
│   ├── main_menu.png
│   ├── student_profile.png
│   ├── calculator_result.png
│   ├── unit_conversion.png
│   ├── geometry_result.png
│   ├── salary_report.png
│   ├── marks_summary.png
│   ├── product_bill.png
│   ├── number_utility.png
│   └── invalid_input.png
│
├── requirements.txt
└── README.md

OOP Concepts Used

The project demonstrates fundamental OOP concepts:

Classes and objects

Constructors using __init__()

Encapsulation using private attributes where appropriate

Methods for business logic

Separation of responsibilities

Service classes/modules for application operations

Each module uses at least one class, and business logic is kept inside class methods rather than placing the complete application in a single file.

Application Flow

Program Start
     ↓
Display Main Menu
     ↓
User Selects a Module
     ↓
Display Module Menu
     ↓
User Selects an Operation
     ↓
Perform Operation
     ↓
Display Result
     ↓
Return to Module Menu / Main Menu
     ↓
Exit

The application continues running until the user selects Exit, allowing multiple modules and operations to be used during the same execution.

Input Validation

The application handles invalid scenarios such as:

Text entered where a number is required

Invalid menu selections

Division or modulus by zero

Negative salary values

Marks below 0 or above 100

Negative product quantity

Negative product price

Discount above 100%

Zero or negative circle radius

Blank required text input

Invalid input should display a helpful message without crashing the application.

Installation

1. Clone the repository

git clone <your-repository-url>

2. Open the project folder

cd Day1_Assignment

3. Install dependencies

pip install -r requirements.txt

If the project does not require external packages, requirements.txt can remain empty.

How to Run

Run the application from the project root:

python main.py

The application starts from main.py, which contains the central menu and navigation logic.

Testing

The project includes testing scenarios for both valid and invalid inputs.

Examples include:

Percentage of 85 produces Excellent

Percentage below 60 produces Not Eligible for placement

Division by zero displays an error

Celsius value 30 converts to Fahrenheit value 86

Negative radius is rejected

Valid salary inputs produce the correct net salary

One subject below 40 produces Fail

Marks above 100 are rejected

Discount above 100% is rejected

Sum of digits of 458 produces 17

Invalid main-menu options display an error

Multiple operations can be performed without restarting the application

Coding Standards

The project follows these practices:

Meaningful variable, class, and method names

PascalCase for class names

snake_case for variables, methods, and file names

Uppercase names for constants

Consistent indentation

Methods focused on one responsibility

Avoidance of repeated code

Comments only where clarification is required

Docstrings for important classes and methods

Author

Neha Mupparthy

Assignment

Python / OOP Console Application Assignment
