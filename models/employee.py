"""Employee identity data."""

class Employee:
    def __init__(self, employee_id, name, basic_salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__basic_salary = basic_salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_basic_salary(self):
        return self.__basic_salary