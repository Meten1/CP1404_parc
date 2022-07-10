import random

from prac_08.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        self.reliability = reliability
        super().__init__(name, fuel)

    def __str__(self):
        return "Your car's reliability is {}, and your car has driven {} km".format(self.reliability, self.odometer)

    def drive(self, distance):
        number = random.randint(0, 101)
        if number < self.reliability:
            distance_driven = distance
        else:
            distance_driven = 0
        super().drive(distance_driven)








