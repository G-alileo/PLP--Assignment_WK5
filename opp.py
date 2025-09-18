# Assignment 1:

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self._battery_life = battery_life  # Encapsulated attribute

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def get_battery_life(self):
        return self._battery_life

    def set_battery_life(self, value):
        if value >= 0:
            self._battery_life = value
        else:
            print("Battery life cannot be negative.")

# Subclass demonstrating inheritance and polymorphism
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu):
        super().__init__(brand, model, battery_life)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

    # Polymorphism: override call method
    def call(self, number):
        print(f"Calling {number} with gaming enhancements from {self.brand} {self.model}...")

# Example usage
phone = Smartphone("Apple", "iPhone 14", 20)
phone.call("123-456-7890")
print("Battery life:", phone.get_battery_life())

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 30, "Adreno 730")
gaming_phone.call("987-654-3210")
gaming_phone.play_game("PUBG Mobile")