class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullname(self):
        return self.first + self.last

class Developer(Employee):
    raised_amount = 1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev_1 = Developer('Puneeth','Gowda', 50000, 'Python')
dev_2 = Developer('Madhu', 'Maddy', 50000, 'Java')

emp_1 = Employee('Sumanth', 'Arya', 40000)

mgr_1 = Manager('Prakash', 'Gowda', 90000, [dev_1, dev_2])

print(mgr_1.email)
mgr_1.print_emp()
mgr_1.rem_emp(emp_1)
mgr_1.print_emp()
