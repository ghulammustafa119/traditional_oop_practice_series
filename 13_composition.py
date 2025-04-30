# Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.




class Engine():
    def start(self):
        print("Engine has started.")

class Car():
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()

engine_obj = Engine()
car_obj = Car(engine_obj)
car_obj.start_car()