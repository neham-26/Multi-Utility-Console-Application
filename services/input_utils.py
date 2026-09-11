"""Input readers with validation."""
def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: this field cannot be empty.")
def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Error: please enter a whole number.")
def read_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Error: please enter a valid number.")