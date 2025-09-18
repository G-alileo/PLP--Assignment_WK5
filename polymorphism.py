
# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Example usage (runs on import or script execution)
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()