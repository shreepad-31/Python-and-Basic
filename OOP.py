class Car:
    total_car = 0 #Class Variable

    def __init__(self, brand, model):
        self.__brand = brand #Encapsulation of brand
        self.__model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}" #Encapsulation of brand
    
    def get_brand(self):
        return self.__brand #Encapsulation of brand, it can be accessed through get_brand
    
    def fuel_type(self): #Polymorphism
        return "Petrol or Diesel"
    
    @property #Read only and can be called as object
    def model(self):
        return self.__model

    @staticmethod #Static Method
    def gen_descrip(): #Don't write "self"
        return "Car are means of transport."

class ElectricCar(Car): #Inheritance
    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model) #Inheritance

        self.battery_size = battery_size

    def fuel_type(self): #Polymorphism
        return "Electricity"

my_ECar = ElectricCar("Tesla", "Model S", "85kWh")
print(my_ECar.get_brand(), my_ECar.model, my_ECar.battery_size)
print(my_ECar.fuel_type())

car_01 = Car("Toyota", "Corolla")
print(car_01.get_brand())
print(car_01.model)
print(car_01.fuel_type())

car_02 = Car("Tata", "Safari")
print(car_02.full_name())

print(Car.total_car)
print(Car.gen_descrip())

# car_01.model = "City" --> It can't happen since model is now read only

print(isinstance(my_ECar, Car))
print(isinstance(my_ECar, ElectricCar))

class Battery:
    def battery_stat(self):
        return "Battery is fine, no worries!"
class Engine:
    def engine_stat(self):
        return "Engine is fine, no worries!"
class EV(Battery, Engine, Car): #Multiple Inheritance
    pass

my_ev = EV("Tesla", "Cybertruck")
print(my_ev.battery_stat())
print(my_ev.engine_stat())