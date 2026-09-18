# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_count=0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
        Car.total_count += 1


car1 = Car("Toyota", "Fortuner")
car2 = Car("Mahindra", "Thar")
car3 = Car("Mercedes", "Model3")

print(Car.total_count)
                     