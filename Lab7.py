# Program Name: Lab7.py
# Course: IT1114/Section XXX
# Student Name: DAniel Urdaneta
# Assignment Number: Lab7
# Due Date: 10/20/2024
# Purpose: This program defines a Worker class that handles a worker's hourly salary, 
# overtime salary, and calculates total pay.
# List specific resources used to complete the assignment: N/A

class Worker:
    def __init__(self, employee_number=0, office_number=0, hours_worked=0, overtime=0):
        self.employee_number = employee_number
        self.office_number = office_number
        self.hours_worked = hours_worked
        self.overtime = overtime
        self.hourly_salary = 0.0
        self.overtime_salary = 0.0
        self.first_name = ""
        self.last_name = ""

    def set_employee_number(self, num):
        """Sets the worker's employee number."""
        self.employee_number = num

    def get_employee_number(self):
        """Returns the worker's employee number."""
        return self.employee_number

    def set_office_number(self, num):
        """Sets the worker's office number."""
        self.office_number = num

    def get_office_number(self):
        """Returns the worker's office number."""
        return self.office_number

    def set_hourly_salary(self, x):
        """Sets the worker's hourly salary. Returns False if salary is less than zero."""
        if x < 0:
            return False
        self.hourly_salary = x
        return True

    def set_overtime_salary(self, x):
        """Sets the worker's overtime salary. Returns False if salary is less than zero."""
        if x < 0:
            return False
        self.overtime_salary = x
        return True

    def get_hourly_salary(self):
        """Returns the worker's hourly salary."""
        return self.hourly_salary

    def get_overtime_salary(self):
        """Returns the worker's overtime salary."""
        return self.overtime_salary

    def set_name(self, *args):
        """Sets the worker's name. Handles both full name and first/last name formats."""
        if len(args) == 1:
            full_name = args[0].split(" ")
            self.first_name = full_name[0]
            self.last_name = full_name[1] if len(full_name) > 1 else ""
        elif len(args) == 2:
            self.first_name = args[0]
            self.last_name = args[1]

    def get_name(self):
        """Returns the worker's full name."""
        return f"{self.first_name} {self.last_name}".strip()

    def get_pay(self):
        """Calculates and returns the worker's total pay."""
        total_pay = (self.hours_worked * self.hourly_salary) + (self.overtime * self.overtime_salary)
        return total_pay

# Example usage
if __name__ == "__main__":
    worker = Worker(employee_number=1000, office_number=359, hours_worked=40, overtime=5)
    worker.set_name("Bob", "Brown")
    worker.set_hourly_salary(15)
    worker.set_overtime_salary(22.5)
    print("Employee Name:", worker.get_name())
    print("Employee Number:", worker.get_employee_number())
    print("Office Number:", worker.get_office_number())
    print("Hourly Salary:", worker.get_hourly_salary())
    print("Overtime Salary:", worker.get_overtime_salary())
    print("Total Pay:", worker.get_pay())
