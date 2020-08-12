class Employee:
    raised_amount = 1000
    def __init__(self, pay):
        self.pay = pay

    def emp_pay(self):
        return self.raised_amount

    @classmethod
    def set_class_variable_value(cls):
        cls.raised_amount = 5000

emp_1 = Employee(5000)
emp_1.raised_amount = 2000
print(emp_1.emp_pay())


print(Employee.raised_amount)

Employee.set_class_variable_value()
print(Employee.raised_amount)


