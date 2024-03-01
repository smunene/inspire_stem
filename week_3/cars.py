#this is a class that describes cars
class car:
    def __init__(self,model, make, year_of_production, fuel_capacity, colour, horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power = horse_power
    def print_make(self,make):
        print("The car is of {0} make".format (self.make))

    def set_make(self,make):
        self.make = make
    def get_make(self):
        return self.make
    
    def set_colour(self,colour):
        self.colour = colour
    def get_colour(self):
        return self.colour


my_car = car("Impalla" , "Chevrolet" , "1969" , "2500 cc", "lilac" , "230 HP")
f_car = car("Note" , "Nissan" , "1973" , "1900 cc", "black" , "150 HP")
my_car.print_make("Nissan")

my_car.set_make("Ford")
f_car.set_make("Toyota")
print(my_car.get_make())
print(f_car.get_make())

my_car.set_colour("grey")
f_car.set_colour("blue")
print(my_car.get_colour())
print(f_car.get_colour())
