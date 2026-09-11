# conversion_service.py
def run_conversion_module():
    print("Unit Converter module under construction.")

""" Temperature and Time Conversion Module """

from services.input_utils import read_float, read_int

class UnitConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def minutes_to_hours(self, total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return hours, minutes

    def days_to_ymd(self, total_days):
        years = total_days // 365
        leftover_days = total_days % 365
        months = leftover_days // 30
        days = leftover_days % 30 
        return years, months, days

def run_conversion_module():
    converter = UnitConverter()
    while True:
        print("**** Unit Converter Module ****")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Minutes to Hours and Minutes")
        print("4. Days to Years, Months, and Days")
        print("5. Return to Main Menu")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            celsius = read_float("Enter temperature in Celsius: ")
            fahrenheit = converter.celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F.")
        elif choice == '2':
            fahrenheit = read_float("Enter temperature in Fahrenheit: ")
            celsius = converter.fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C.")
        elif choice == '3':
            total_minutes = read_int("Enter total minutes: ")
            hours, minutes = converter.minutes_to_hours(total_minutes)
            print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes.")
        elif choice == '4':
            total_days = read_int("Enter total days: ")
            years, months, days = converter.days_to_ymd(total_days)
            print(f"{total_days} days is {years} years, {months} months, and {days} days.")
        elif choice == '5':
            return  # Return to the main menu
        else:
            print("Invalid option. Choose 1 to 5.")