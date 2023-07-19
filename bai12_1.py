# OOP Exercise - Exercise 1: Create a Class with instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(300, 30)
print(car.max_speed, car.mileage)