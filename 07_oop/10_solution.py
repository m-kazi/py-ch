class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


# extending class 'Car, Battery, Engine' here as multiple inheritance
class ElectricCar(Battery, Engine, Car):
    pass


my_tesla = ElectricCar("Tesla", "Model S")

print(my_tesla.engine_info())
print(my_tesla.battery_info())
