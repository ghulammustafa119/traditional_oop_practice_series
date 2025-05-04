# Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.



class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self):
        self.engine = Engine()  

    def start_car(self):
        print("Starting the car...")
        self.engine.start()

car_obj = Car()
car_obj.start_car()
