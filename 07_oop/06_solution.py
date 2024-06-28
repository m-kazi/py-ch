class Car:
    # clas variable to count total car created
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullname(self):
        return f"{self.brand} : {self.model}"


nissan = Car("Nissan", "GTR")
bmw = Car("BMW", "M5")
toyota = Car("Toyota", "Supra")

print(nissan.brand)
print(bmw.brand)
print(toyota.brand)
print(f"Total car created: {Car.total_car}")
