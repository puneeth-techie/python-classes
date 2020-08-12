class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def employee_name(self, first):
        return f'{first} {self.last}'

emp_1 = Employee('Puneeth', 'Gowda', 30000)
emp_2 = Employee('Madhu', 'Maddy', 30000)

print(emp_1.first)
print(emp_2.first + emp_2.last)
print(emp_2.email)

print(emp_1.employee_name('PPG'))
print(emp_2.employee_name('MM'))

