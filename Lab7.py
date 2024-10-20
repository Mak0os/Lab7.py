# Program Name: Lab7.py
# Course: IT1114/Section XXX
# Student Name: DAniel Urdaneta
# Assignment Number: Lab7
# Due Date: 10/20/2024
# Purpose: This program defines a Worker class that handles a worker's hourly salary, 
# overtime salary, and calculates total pay.
# List specific resources used to complete the assignment: N/A

class Worker:
    # Constructor (__init__): Initializes all attributes with default values.
    def __init__(self):
        self.employee_number = None
        self.office_number = None
        self.name = {'first': '', 'last': ''}
        self.birthdate = {'day': 0, 'month': 0, 'year': 0}
        self.total_hours_worked = 0
        self.total_overtime_hours = 0
        self.hourly_salary = 0.0  # New attribute for hourly salary
        self.overtime_salary = 0.0  # New attribute for overtime salary

    # Existing methods...

    # get_employee_number(): Returns the worker's employee number.
    def get_employee_number(self):
        return self.employee_number

    # set_employee_number(x): Sets the worker's employee number to the given value 'x'.
    def set_employee_number(self, x):
        self.employee_number = x

    # get_office_number(): Returns the worker's office number.
    def get_office_number(self):
        return self.office_number

    # set_office_number(x): Sets the office number to the given value 'x'.
    def set_office_number(self, x):
        if 100 <= x <= 500:
            self.office_number = x
            return True
        else:
            return False

    # get_name(): Returns the worker's full name in the format "First Last".
    def get_name(self):
        return f"{self.name['first']} {self.name['last']}"

    # set_name(first_name, last_name): Sets the worker's first and last name.
    def set_name(self, first_name, last_name):
        self.name['first'] = first_name
        self.name['last'] = last_name

    # set_birthdate(d, m, y): Sets the worker's birthdate.
    def set_birthdate(self, d, m, y):
        if 1 <= m <= 12 and 1 <= d <= 31:
            self.birthdate['day'] = d
            self.birthdate['month'] = m
            self.birthdate['year'] = y
            return True
        else:
            return False

    # get_hours_worked(): Returns the total number of regular hours worked.
    def get_hours_worked(self):
        return self.total_hours_worked

    # add_hours(x): Adds 'x' hours to the worker's total hours worked.
    def add_hours(self, x):
        if x > 9:
            self.total_hours_worked += 9
            self.total_overtime_hours += (x - 9)
        else:
            self.total_hours_worked += x

    # get_hours_overtime(): Returns the total number of overtime hours worked.
    def get_hours_overtime(self):
        return self.total_overtime_hours

    # New methods for hourly salary and overtime salary
    def set_hourly_salary(self, x):
        """Sets the worker’s hourly salary. Returns False if salary is less than zero."""
        if x < 0:
            return False
        self.hourly_salary = x
        return True

    def set_overtime_salary(self, x):
        """Sets the worker’s overtime salary. Returns False if salary is less than zero."""
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

    def get_pay(self):
        """Returns the worker’s total pay based on hours worked and overtime."""
        return (self.total_hours_worked * self.hourly_salary) + (self.total_overtime_hours * self.overtime_salary)

# Example usage of the Worker class (for testing purposes):
if __name__ == "__main__":
    worker = Worker()
    
    # Set employee information
    worker.set_employee_number(12345)
    worker.set_office_number(250)
    worker.set_name("John", "Doe")
    worker.set_birthdate(12, 5, 1990)

    # Set salaries
    worker.set_hourly_salary(20)  # $20 per hour
    worker.set_overtime_salary(30)  # $30 per overtime hour

    # Add hours worked and print results
    worker.add_hours(12)  # 9 regular hours, 3 overtime

    # Display information
    print("Employee Number:", worker.get_employee_number())
    print("Office Number:", worker.get_office_number())
    print("Name:", worker.get_name())
    print("Birthdate:", worker.birthdate)
    print("Hourly Salary:", worker.get_hourly_salary())
    print("Overtime Salary:", worker.get_overtime_salary())
    print("Hours Worked:", worker.get_hours_worked())
    print("Overtime Hours:", worker.get_hours_overtime())
    print("Total Pay:", worker.get_pay())
