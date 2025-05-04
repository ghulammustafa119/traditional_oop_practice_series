# Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee():
    def __init__(self, name, emp_id,):
        self.name = name
        self.emp_id = emp_id
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Id: {self.emp_id}")

class Department():
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee
    def display_department(self):
        print(f"Department Name: {self.department_name}")
        self.employee.display_info()

emp1 = Employee("Mustafa",51214)
dept1 = Department("IT",emp1)
dept1.display_department()
del dept1
print("\nEmployee still exists after Department is deleted:")
emp1.display_info()    