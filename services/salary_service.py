#salary_service.py
def run_salary_module():
    print("Salary module under construction.")

"""Salary report using Employee + calculation class."""

from models.employee import Employee
from services.input_utils import read_text, read_float


class EmployeeSalary:
    def __init__(self, employee, allowance_pct, bonus_pct, deduction_pct):
        self.__employee = employee
        self.__allowance_pct = allowance_pct
        self.__bonus_pct = bonus_pct
        self.__deduction_pct = deduction_pct

    def calculate_allowance(self):
        basic = self.__employee.get_basic_salary()
        return basic * self.__allowance_pct / 100

    def calculate_bonus(self):
        basic = self.__employee.get_basic_salary()
        return basic * self.__bonus_pct / 100

    def calculate_gross(self):
        basic = self.__employee.get_basic_salary()
        return basic + self.calculate_allowance() + self.calculate_bonus()

    def calculate_deduction(self):
        return self.calculate_gross() * self.__deduction_pct / 100

    def calculate_net_salary(self):
        return self.calculate_gross() - self.calculate_deduction()

    def display_report(self):
        emp = self.__employee

        print()
        print("=" * 40)
        print(" SALARY REPORT")
        print("=" * 40)

        print(f"Employee ID    : {emp.get_employee_id()}")
        print(f"Name           : {emp.get_name()}")
        print(f"Basic Salary   : {emp.get_basic_salary():.2f}")
        print(f"Allowance      : {self.calculate_allowance():.2f}")
        print(f"Bonus          : {self.calculate_bonus():.2f}")
        print(f"Gross Salary   : {self.calculate_gross():.2f}")
        print(f"Deduction      : {self.calculate_deduction():.2f}")
        print(f"Net Salary     : {self.calculate_net_salary():.2f}")

        print("=" * 40)


def _non_negative(prompt):
    while True:
        value = read_float(prompt)

        if value >= 0:
            return value

        print("Error: value cannot be negative.")


def run_salary_module():
    employee_id = read_text("Employee ID: ")
    name = read_text("Employee name: ")

    basic = _non_negative("Basic salary: ")
    allowance_pct = _non_negative("Allowance percentage: ")
    bonus_pct = _non_negative("Bonus percentage: ")
    deduction_pct = _non_negative("Deduction percentage: ")

    employee = Employee(employee_id, name, basic)

    salary = EmployeeSalary(
        employee,
        allowance_pct,
        bonus_pct,
        deduction_pct
    )

    salary.display_report()
