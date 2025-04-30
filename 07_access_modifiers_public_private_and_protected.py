# Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.






class Employee():
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

employee1 = Employee("Mustafa", 70000, "123-456-7890")
print(f"Name: {employee1.name}")
print(f"Salary: {employee1._salary}")
# print(f"SSN (using name mangling): {employee1._Employee__ssn}") 

try:
    print(f"SSN: {employee1.__ssn}")

except AttributeError as e:
    print(f"Error accessing private variable: {e}")

print(f"SSN (using name mangling): {employee1._Employee__ssn}")  # output (Name: Mustafa  Salary: 70000  Error accessing private variable: 'Employee' object has no attribute '__ssn'  SSN (using name mangling): 123-456-7890).