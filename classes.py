class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = "$" + str(salary)
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}" .format(self.first, self.last)
    
    
emp_1 = Employee('John', 'Storm', 50000)        

print(emp_1.email)
print(emp_1.salary)
print(emp_1.fullname())
