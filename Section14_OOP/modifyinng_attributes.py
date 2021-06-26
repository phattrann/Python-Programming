class Car:
    def __init__(self, model, year, price):     # Instance attributes
        # __ is object attributes use for private attribute
        self.__model = model
        self.year = year
        self.price = price
    wheels = 4          # Class attributes

    def setmodel(self, model):  # setters
        self.__model = model
    def getmodel(self):         # getters
        return self.__model

    model = property(getmodel, setmodel)

car1 = Car("BMW", 2014, 10000)
car2 = Car("Mes", 2015, 60000)
print(car1 == car2)
# print(car1.setmodel("AAA"))
# print(car1.getmodel())

car1.model = "AAA"
print(car1.model)