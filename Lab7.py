# Program Name: Lab7.py
# Course: IT1114/Section XXX
# Student Name: DAniel Urdaneta
# Assignment Number: Lab7
# Due Date: 10/20/2024
# Purpose: This program defines a Worker class that handles a worker's hourly salary, 
# overtime salary, and calculates total pay.
# List specific resources used to complete the assignment: N/A

class Worker:
    def __init__(self, hours_worked=0, overtime=0):
        self.hours_worked = hours_worked
        self.overtime = overtime
        self.hourly_salary = 0.0
        self.overtime_salary = 0.0

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

    def get_pay(self):
        """Calculates and returns the worker's total pay."""
        total_pay = (self.hours_worked * self.hourly_salary) + (self.overtime * self.overtime_salary)
        return total_pay

# Example usage
if __name__ == "__main__":
    worker = Worker(hours_worked=40, overtime=5)
    worker.set_hourly_salary(15)
    worker.set_overtime_salary(22.5)
    print("Hourly Salary:", worker.get_hourly_salary())
    print("Overtime Salary:", worker.get_overtime_salary())
    print("Total Pay:", worker.get_pay())
