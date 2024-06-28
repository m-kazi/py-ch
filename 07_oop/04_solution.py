class Car:
    def __init__(self, brand, model):
        # making 'brand' a private variable with '__'
        self.__brand = brand
        self.model = model

    # encapsulation 'brand' & getter method
    def get_brand(self):
        return self.__brand + " !"


my_car = Car("BMW", "335xi")
# print(my_car.__brand)
print(my_car.get_brand())
