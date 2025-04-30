# callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.





class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

#  Create an object
m = Multiplier(5)

#  Test with callable()
print(callable(m))     # True, kyun ke __call__() method defined hai

#  Call the object like a function
result = m(10)         # yeh m.__call__(10) ka short form hai
print(result)          # 50
