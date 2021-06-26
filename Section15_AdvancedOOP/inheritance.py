## Car Class
class Vehicle:
    def __init__(self,model, year):
        self.model = model
        self.year = year
    
    def print_veh(self):
        print("I am a veh")
    
class Car(Vehicle):
    def __init__(self, model, year, price):
        super().__init__(model, year)
        self.price = price
    ## method overriding
    def print_veh(self):
        print("I am a car")
    ## method adding
    def discount(self, dis):
        ## super function
        super().print_veh()
        return self.price*(1-dis)
        
    
car1 = Car("BMW", 2021, 100000)

print(car1.discount(0.2))


## multiple inheritance
class Factory:
    def print_fac(self):
        print("this is a fac")

class Bike(Vehicle, Factory):
    def __init__(self, model, year, location):
        super().__init__(model, year)
        self.location = location
    def print_bike(self):
        print("This bike")

bike = Bike("BMW", 2021, "HCM")
print(bike.print_fac())