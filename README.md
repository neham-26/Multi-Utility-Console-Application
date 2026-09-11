# Multi-Utility Console Application
Assignment 1 — a menu-driven Python console app with eight utilities.  
One entry point (`main.py`). Each module uses **classes and objects**.
Copy this file into your project folder as `README.md` (replace the author name at the bottom).
---
## Project Overview
This program is a **Swiss-army knife of small tools** behind one main menu. The user runs a single command, picks a tool (student profile, calculator, converter, and so on), enters values, and sees a formatted report. The menu stays open until **Exit**, so several tools can be used in one run.
The code is split on purpose:
- `main.py` — navigation only (the remote control)
- `models/` — data classes (`Student`, `Employee`, `Product`)
- `services/` — menus, input, and business logic classes
---
## Features
- Central main menu with 8 modules + Exit
- Object-oriented design (`__init__`, private attributes, methods)
- Input validation (empty text, non-numbers, out-of-range values)
- Safe calculator (no crash on divide / modulus by zero)
- Formatted reports (student profile, salary, marks, product bill)
- Return-to-main-menu from every submodule
---
## Prerequisites
- Python **3.10** or newer
- VS Code (or any editor)
- Windows, macOS, or Linux terminal
No extra packages. The standard library is enough (`math` for geometry).
---
## Installation / setup
1. Install Python from [python.org](https://www.python.org/downloads/). Tick **Add Python to PATH**.
2. Open a terminal and check:
   ```bash
   python --version
   ```
   If that fails, use `python3 --version`.
3. Open the project folder in VS Code:
   **File → Open Folder → Assignment 1**
   The folder that contains `main.py` must be the one you open (not a parent folder).
4. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
   Windows: `.venv\Scripts\activate`  
   macOS/Linux: `source .venv/bin/activate`
`requirements.txt` records that **no third-party libraries** are required.
---
## How to run (usage)
From the project root (the folder that contains `main.py`):
```bash
python main.py
```
or:
```bash
python3 main.py
```
**Do not** run files inside `models/` or `services/` directly.
Then type a number **1–9**:
| Choice | Module |
|--------|--------|
| 1 | Student Profile Management |
| 2 | Calculator Operations |
| 3 | Unit Converter |
| 4 | Geometry Calculator |
| 5 | Salary Calculator |
| 6 | Marks Analyzer |
| 7 | Product Billing System |
| 8 | Number Utilities |
| 9 | Exit |
Invalid choices (for example `10` or `abc`) print an error and show the menu again. The app does not crash.
---
## Project structure
```text
Assignment 1/
├── main.py                      # Entry point — main menu loop
├── models/
│   ├── __init__.py              # Marks this folder as a package
│   ├── student.py               # class Student
│   ├── employee.py              # class Employee
│   └── product.py               # class Product
├── services/
│   ├── __init__.py
│   ├── input_utils.py           # Safe read_text / read_int / read_float
│   ├── student_service.py
│   ├── calculator_service.py    # class Calculator
│   ├── conversion_service.py    # class UnitConverter
│   ├── geometry_service.py      # class GeometryCalculator
│   ├── salary_service.py        # class EmployeeSalary
│   ├── marks_service.py         # class MarksAnalyzer
│   ├── billing_service.py       # class ProductBilling
│   └── number_service.py        # class NumberUtility
├── screenshots/                 # Demo images (see below)
├── requirements.txt
├── .gitignore
└── README.md
```
**Why this split**
| Place | Job |
|--------|-----|
| `main.py` | Show the remote (menu), call one module, loop until Exit |
| `models/` | Remember data (name, salary, product fields) |
| `services/` | Talk to the user and run formulas |
| `__init__.py` | Empty files so Python can `import` from the folder |
---
## Modules and formulas
### 1. Student Profile Management
**Class:** `Student` in `models/student.py`  
**Flow:** `student_service.py` reads input → creates a `Student` object → `display_profile()`.
**Inputs:** name, age, college, branch, academic year, percentage.
**Performance (check from high to low):**
| Percentage | Performance |
|------------|-------------|
| 85 and above | Excellent |
| 70 to 84.99 | Good |
| 55 to 69.99 | Developing |
| 40 to 54.99 | Needs Improvement |
| Below 40 | Poor |
**Placement eligibility (both must be true):**
- Percentage **≥ 60**, **and**
- Academic year is **Third Year** or **Fourth Year**
Otherwise: **Not Eligible**.
Sample: Rahul Sharma, 21, ABC College, Computer Science, Fourth Year, 78.50% → **Good**, **Eligible**.
---
### 2. Calculator Operations


