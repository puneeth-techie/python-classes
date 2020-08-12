class Employee:

    @classmethod
    def add_emp(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+'@gmail.com'

name = 'John-Doe-7000'
emp_1 = Employee.add_emp(name)

print(emp_1.email)
print(emp_1.pay)
