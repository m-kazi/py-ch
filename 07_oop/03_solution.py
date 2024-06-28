class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# extending class 'Car' here
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fullname(self):
        return f"{self.brand} : {self.model} : {self.battery_size}"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(my_tesla.fullname())
print(my_tesla.brand)
