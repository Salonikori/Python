# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def desc():
        return "Cars are Awesome"


car1 = Car("Toyota", "Fortuner")

print(car1.brand)
print(car1.model)
print(car1.desc())