#geometry_service.py
def run_geometry_module():
    print("Geometry module under construction.")

""" Area, perimeter, and circumference calculations. """

import math 

from services.input_utils import read_float

class GeometryCalculator:
    def rectangle_area(self, lenght, width):
        return lenght * width

    def rectangle_perimeter(self, lenght, width):
        return 2 * (lenght + width)

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def circle_circumference(self, radius):
        return 2 * math.pi * radius

def _positive(prompt):
    while True:
        value = read_float(prompt)
        if value > 0:
            return value
        print("Error: value must be greater than zero.")

def run_geometry_module():
    geometry = GeometryCalculator()

    while True:
        print("**** Geometry Module ****")
        print("1. Rectangle Area")
        print("2. Rectangle Perimeter")
        print("3. Circle Area")
        print("4. Circle Circumference")
        print("5. Return to Main Menu")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            length = _positive("Enter the length of the rectangle: ")
            width = _positive("Enter the width of the rectangle: ")
            area = geometry.rectangle_area(length, width)
            print(f"Area of rectangle: {area}")
        elif choice == '2':
            length = _positive("Enter the length of the rectangle: ")
            width = _positive("Enter the width of the rectangle: ")
            perimeter = geometry.rectangle_perimeter(length, width)
            print(f"Perimeter of rectangle: {perimeter}")
        elif choice == '3':
            radius = _positive("Enter the radius of the circle: ")
            area = geometry.circle_area(radius)
            print(f"Area of circle: {area}")
        elif choice == '4':
            radius = _positive("Enter the radius of the circle: ")
            circumference = geometry.circle_circumference(radius)
            print(f"Circumference of circle: {circumference}")
        elif choice == '5':
            return  # Return to main menu
        else:
            print("Invalid option. Choose 1 to 5.")