"""User flow for student profiles."""
from models.student import Student
from services.input_utils import read_text, read_int, read_float

def run_student_module():
    print()
    print("Enter student details")
    name = read_text("Name: ")
    age = read_int("Age: ")
    if age <= 0:
        print("Error: age must be a positive number.")
        return
    college = read_text("College: ")
    branch = read_text("Branch: ")
    academic_year = read_text("Academic year (example: Fourth Year): ")
    percentage = read_float("Percentage: ")
    if percentage < 0 or percentage > 100:
        print("Error: percentage must be between 0 and 100.")
        return
    student = Student(name, age, college, branch, academic_year, percentage)
    student.display_profile() 