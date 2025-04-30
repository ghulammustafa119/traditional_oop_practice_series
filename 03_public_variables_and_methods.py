# Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car():
    brand = "Suzuki"
    def start(self):
        print(f"The {self.brand} Car is Starting!")
my_car = Car()
print(my_car.brand)
my_car.start()    