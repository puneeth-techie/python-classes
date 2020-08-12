class Employee:

    raised_amount = 1000

    def __init__(self, first, pay):
        self.first = first
        self.pay = pay

    def employee_pay(self):
        return self.pay + self.raised_amount

emp_1 = Employee('Puneeth', 5000)

print(Employee.raised_amount)
print(Employee.__dict__)
emp_1.raised_amount = 2000
print(emp_1.raised_amount)
print(emp_1.__dict__)
print(emp_1.employee_pay())
