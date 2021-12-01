import random

n = [i for i in range(14) if i != 11]
uni_cards = {
    'hearts': {v+1: chr(127153 + n[v]) for v in range(13)},
    'spades': {v+1: chr(127137 + n[v]) for v in range(13)},
    'face_down': chr(127136)
}

class Card:
    """
    Modelliert eine Karte
    """
    def __init__(self, value, color):
        self._value = value
        self._color = color
        #@ToDo counter for max number of card for safety ...
        if self._value < 1 or self._value > 13:
            raise Exception("The card Value is false")
        if self._color != "hearts" and self._color != "spades":
            raise Exception("The color of card is not spades or hearts, it is : ", self._color )

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def set_value(self, value):
        self._value = value

    def set_color(self, color):
        self._color = color

    def fits_to(self, drop_card):
        return self._value == drop_card - 1

    def __str__(self):
        return uni_cards[self.get_color()][self.get_value()]

#Funktionalyty Test done
if __name__ == "__main__":
    s = Card(10, "spades")
    s_2 = Card(11, "spades")
    print(s.fits_to(s_2.get_value()))
