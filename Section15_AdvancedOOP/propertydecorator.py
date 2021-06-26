lass Car:
    count_car = 0
    def __init__(self, model):
        self.__model = model
        Car.count_car = Car.count_car + 1

    @property       # getter
    def x(self):
        return self.__model

    @x.setter       # setter
    def model(self, model):
        self.__model = model

    # Access only to the class
    @classmethod
    def countcars(car_class):
        print("We have: ", car_class.count_car)

    # Access to nothing in the class
    @staticmethod
    def peep():
        print("Peepp")

car1 = Car("BMW")

print(car1.peep())
car1.model = "Audi"

print(Car.countcars())

class House:
    def __init__(self, rooms, kitchens, acreage, peopleinDafam):
        self.__room = rooms
        self.__kitchen = kitchens
        self.__acreage = acreage
        self.people = peopleinDafam
    # Cach 1
    @property
    def getroom(self):
        return self.__room
    
    @getroom.setter
    def room(self, rooms):
        self.__room = rooms

    # Cach 2
    def getkitchen(self):
        return self.__kitchen
    def setkitchen(self,x):
        self.__kitchen = x
    
    
    # Cach 3
    def getacreage(self):
        return self.__acreage

    def setacreage(self, x):
        self.__acreage = x
    acreage = property(getacreage, setacreage)

phumyhung = House(5,2, 250,5)
phumyhung.acreage = 300
print(phumyhung.acreage)
phumyhung.people = 10
print(phumyhung.people)


        