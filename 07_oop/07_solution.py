class Car:
    # clas variable to count total car created
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    # static method
    @staticmethod
    def general_desc():
        return "Cars are awesome !"


nissan = Car("Nissan", "GTR")

print(nissan.general_desc())
