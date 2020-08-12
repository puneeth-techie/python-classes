class Employee:
    
    no_of_employee = 0

    # Regular method of class and we should pass self as an first argument
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    no_of_employee += 1

    @classmethod
    def add_employee(cls, emp_details):
        first, last, pay = emp_details.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

details = 'John-Doe-7000'
emp_1 = Employee.add_employee(details)
print(emp_1.first+emp_1.last)
print(Employee.no_of_employee)
import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

