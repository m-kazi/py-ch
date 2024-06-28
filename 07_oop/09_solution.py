class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# extending class 'Car' here
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("BMW", "X5")
my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# checking the instance
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))

# print(my_tesla.brand)
