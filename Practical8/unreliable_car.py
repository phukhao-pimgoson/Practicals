from random import randint
from Practical8.car import Car


class Unreliable(Car):
    def __init__(self, name, fuel, reliable):
        super(Unreliable, self).__init__(name, fuel)
        self.reliable = reliable

    def drive(self, distance):
        number = randint(1, 100)
        if number >= self.reliable:
            distance = 0
        driven = super().drive(distance)
        return driven
