from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string like the original Taxi but with flagfall."""
        return f"{super().__str__()}, flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the silverservicetaxi trip."""
        return self.flagfall + super().get_fare()