class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("BMW", "335xi")
print(my_car.brand)
print(my_car.model)


new_car = Car("Toyota", "Corolla")
print(new_car.brand)
print(new_car.model)
