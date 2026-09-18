# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "I am a battery"

class Engine:
    def engine_info(self):
        return "I am a Engine"

class ElectricCar(Battery, Engine):
    pass

car1 = ElectricCar()
print(car1.battery_info())
print(car1.engine_info())