from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = 4.50
        self.price_per_km *= fanciness

    def __str__(self):

        return "{}, ${:.2f}/km plus flagfall of $4.50".format(super().__str__(), self.price_per_km)

    def get_fare(self):
        return self.flagfall + super().get_fare()


