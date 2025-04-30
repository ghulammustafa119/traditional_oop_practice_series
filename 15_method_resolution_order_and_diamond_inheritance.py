#  Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from venv import create
# from A and override show(),

# D that inherits from both B and C.

# create an object of D and call show() to observe MRO.



class A():
    def show(self):
        print("A.show() called.")

class B(A):
    def show(self):
        print("B.show() called.")

class C(A):
    def show(self):
        print("C.show() called.")

class D(B, C):
    pass

d = D()
d.show()


print(D.__mro__)