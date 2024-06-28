class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # polymorphism: same method different output
    def fuel_type(self):
        return "Petrol or Diesel"


# extending class 'Car' here
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fullname(self):
        return f"{self.brand} : {self.model} : {self.battery_size}"

    # polymorphism: same method different output
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
my_toyota = Car("Toyota", "Corolloa")

print(my_toyota.fuel_type())
print(my_tesla.fuel_type())
