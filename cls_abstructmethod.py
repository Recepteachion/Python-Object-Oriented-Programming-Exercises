
from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ =ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self,miles,make,model,year,sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year  = year
        self.sold_on = sold_on
    def sale_price(self):
        """Return the sale price for this vehicle"""
        if self.sold_on is not None:
            return 0.0
        return 5000.0 * self.wheels
    def purchase_price(self):
        if self.sold_on is None:
            return 0.0 
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4
    def vehicle_type(self):
        return "car"
    
class Truck(Vehicle):
    base_sale_price = 10000
    wheels=4
    def vehicle_type(self):
        return "truck"

class Motorcycle(Vehicle):
    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        return "motorcycle"




veh_1 = Vehicle(miles=5,make="BMW",model="Benz",year=2010,sold_on=None)
print(veh_1.purchase_price())
print("-----------------------")

trc_1 = Truck(miles=50,make="Mercedes",model="McLaren",year=2015,sold_on=True)
print(trc_1.purchase_price())
print("---------------------")
car_1 = Car(10,"Tofaş","Şahin",1995,None)
print(car_1.sale_price())
print("---------------------")
mtr_1 = Motorcycle(15,"BMW","Snake",1998,True)
print(mtr_1.purchase_price())
