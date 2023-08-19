class Car:
    no_of_wheels = 4

    def __init__(self, model, make):
        self.model = model
        self._color = ""
        self.make = make

my_car = Car("Civic","Honda")
my_car_2 = Car("Fit","Honda")

Car.no_of_wheels = 6

print(my_car.no_of_wheels)
print(my_car_2.no_of_wheels)

#@classmethod
#def create_honda(cls, model, color):
 #   return cls(model, color, "Honda")


#@classmethod
#def create_toyota(cls, model, color):
 #   return cls(model, color, "toyota")


#@staticmethod
#def is_toyota(make):
 #   return make == "toyota"