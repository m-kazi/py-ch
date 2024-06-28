class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} : {self.model}"


my_car = Car("BMW", "335xi")
print(my_car.fullname())
