from abc import ABC


class Cloths(ABC):
    def __init__(self, param):
        self.param = param


class Coat(Cloths):
    @property
    def my_method(self):
        return round(self.param / 6.5 + 0.5)


class Suit(Cloths):
    @property
    def my_method(self):
        return round(2 * self.param + 0.3)


coat = Coat(8)
print(f"Расход ткани на пальто: {coat.my_method}")
suit = Suit(10)
print(f"Расход ткани на костюм: {suit.my_method}")
print(f"Суммарный расход ткани: {coat.my_method + suit.my_method}")
