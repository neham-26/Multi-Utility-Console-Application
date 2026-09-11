#marks_service.py
def run_marks_module():
    print("Marks module under construction.")

""" Five-subjects academic summary."""

from services.input_utils import read_text, read_float

class MarksAnalyzer:
    def __init__(self, student_name, subject_marks):
        self.__student_name = student_name
        self.__subject_marks = subject_marks

    def calculate_total(self):
        return sum(self.__subject_marks.values())

    def calculate_average(self):
         return self.calculate_total() / len(self.__subject_marks)

    def highest_mark(self):
        return max(self.__subject_marks.values())

    def lowest_mark(self):
        return min(self.__subject_marks.values())

    def pass_or_fail(self):
        if all(mark >= 40 for mark in self.__subject_marks.values()):
            return "Pass"
        return "Fail"
    
    def performance_level(self):
        avg = self.calculate_average()
        if avg >= 85:
            return "Excellent"
        if avg >= 70:
            return "Good"
        if avg >= 55:
            return "Developing"
        if avg >= 40:
            return "Needs Improvement"
        return "Poor"

    def display_report(self):
        print()
        print("=" * 40)
        print("       MARKS SUMMARY ")
        print("=" * 40)
        print(f"Student: {self.__student_name}")
        for subject, mark in self.__subject_marks.items():
            print(f"{subject:20} : {mark:.2f}")
        print("-" * 40)
        print(f"Total        : {self.calculate_total():.2f}")
        print(f"Average      : {self.calculate_average():.2f}")
        print(f"Highest      : {self.highest_mark():.2f}")
        print(f"Lowest       : {self.lowest_mark():.2f}")
        print(f"Result       : {self.pass_or_fail()}")
        print(f"Performance  : {self.performance_level()}")
        print("=" * 40)

def _read__mark(subject_name):
    while True:
        mark = read_float(f"Marks for {subject_name} (0-100)")
        if 0 <= mark <=100 :
            return mark
        print("Error: mark must be between 0 and 100.")

def run_marks_module():
    name = read_text("Student name : ")
    subject_marks ={}
    for i in range(1,6):
        subject = read_text(f"Subject {i} name: ")
        subject_marks[subject] = _read__mark(subject)

        analyzer = MarksAnalyzer(name, subject_marks)
        analyzer.display_report