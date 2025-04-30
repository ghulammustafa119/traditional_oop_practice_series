# Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.




#  Step 1: Custom Exception Class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above."):
        super().__init__(message)

#  Step 2: Function that raises the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        print("Access granted.")

#  Step 3: Use try-except to handle it
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError caught:", e)
