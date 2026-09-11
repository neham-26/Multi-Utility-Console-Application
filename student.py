"""Student data and academic rules.
Private fields are only read or written through getters and setters.
"""
class Student:
    def __init__(self, name, age, college, branch, academic_year, percentage):
        self.set_name(name)
        self.set_age(age)
        self.set_college(college)
        self.set_branch(branch)
        self.set_academic_year(academic_year)
        self.set_percentage(percentage)

        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def get_college(self):
        return self.__college
    def set_college(self, college):
        self.__college = college
    def get_branch(self):
        return self.__branch
    def set_branch(self, branch):
        self.__branch = branch
    def get_academic_year(self):
        return self.__academic_year
    def set_academic_year(self, academic_year):
        self.__academic_year = academic_year
    def get_percentage(self):
        return self.__percentage
    def set_percentage(self, percentage):
        self.__percentage = percentage
    def determine_performance(self):
        p = self.get_percentage()
        if p >= 85:
            return "Excellent"
        if p >= 70:
            return "Good"
        if p >= 55:
            return "Developing"
        if p >= 40:
            return "Needs Improvement"
        return "Poor"
    def determine_placement_eligibility(self):
        year = self.get_academic_year().strip().lower()
        year_ok = year in ("third year", "fourth year")
        if self.get_percentage() >= 60 and year_ok:
            return "Eligible"
        return "Not Eligible"
    def display_profile(self):
        print()
        print("=" * 40)
        print("           STUDENT PROFILE")
        print("=" * 40)
        print(f"Name            : {self.get_name()}")
        print(f"Age             : {self.get_age()}")
        print(f"College         : {self.get_college()}")
        print(f"Branch          : {self.get_branch()}")
        print(f"Academic Year   : {self.get_academic_year()}")
        print(f"Percentage      : {self.get_percentage():.2f}%")
        print(f"Performance     : {self.determine_performance()}")
        print(f"Placement Status: {self.determine_placement_eligibility()}")
        print("=" * 40) 