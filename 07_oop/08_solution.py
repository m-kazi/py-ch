class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # making 'model' private

    # property decorators to make 'model' attribute read only
    @property
    def model(self):
        return self.__model


nissan = Car("Nissan", "GTR")
# changing the model
# nissan.model = "Juke"
print(nissan.model)
