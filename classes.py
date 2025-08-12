class Employee:

    num_of_emps = 0
    raise_amount = 1.15


    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}" .format(self.first, self.last)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

     

    
    
emp_1 = Employee('John', 'Storm', 50000)        
emp_2 = Employee ("Wade", "Wilson", 3000)

print(emp_1.email)
print(emp_1.salary)
print(emp_1.fullname())
print(emp_2.first)
print(emp_2.email)
print(Employee.num_of_emps)
print(emp_2.fullname())
emp_1.apply_raise() #this is how you use the raise amount function 
print(emp_1.salary)
