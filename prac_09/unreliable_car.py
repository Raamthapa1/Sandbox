from car import Car
from random import randint


class UnreliableCar(Car):
    """unrelaiable car having chance that the drive methid will work"""

    def __init__(self, name, fuel, reliability):
        """New class UnreliableCar that enhirits form Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but depends upon random relaibility."""
        if randint(1, 100) > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


    def __str__(self):
        """Return a string like a Car with reliability."""
        return f"{super().__str__()}, {self.reliability}% reliability"
