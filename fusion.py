
'''
---- Enthält die fertig funktionierende Klassen
'''
n = [i for i in range(14) if i != 11]
uni_cards = {
    'hearts': {v+1: chr(127153 + n[v]) for v in range(13)},
    'spades': {v+1: chr(127137 + n[v]) for v in range(13)},
    'face_down': chr(127136)
}

def create_cards(numbers, value):
    cards = []
    for i  in range(numbers[0], numbers[1] + 1):
        cards.append(Card(i, value))
    return cards

class Card:
    """
    Modelliert eine Karte
    """
    def __init__(self, value, color):
        self._value = value
        self._color = color
        # if type(self._value) type(self._color)
        if self._value < 1 or self._value > 13:
            raise Exception("The card Value is false", self._value)
        if self._color != "hearts" and self._color != "spades":
            raise Exception("The color of card is not spades or hearts, it is : ", self._color)

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def set_value(self, value):
        self._value = value

    def set_color(self, color):
        self._color = color

        # Todo this form drop_card = card [value, color]
    def fits_to(self, drop_card):
        # value_only = self._color == drop_card[1]:
        value_only = False
        if self._color != drop_card.get_color():
            if self._value - 1 == drop_card.get_value():
                value_only = True
        return value_only

    def __str__(self):
        return uni_cards[self.get_color()][self.get_value()]


class Sequence:
    """
     modelliert eine absteigende Sequenz von Karten
    """
# erwartet eine Liste von Card-Instanzen
    def __init__(self, cards):
        self._cards = cards

    def first_card(self):
        return self._cards[0]

    def last_card(self):
        return self._cards[-1]

    def get_card_seq(self, index):
        return self._cards[index]

    # ToDo check Attribut card_in, bzw ob carten zu einander passen
    # Todo prüfe ob input card dem Standart entspricht lst, values grenzen
    def append_card(self, card):
        # return nötig ?
        self._cards.append(card)

# first card is
    def fits_to(self, cards):
        return int(self._cards.last_card.get_value()) - 1 == int(cards.first_card().get_value())

    def merge(self, cards_to_merge):
        # fits to nötig ??
        # neue sequenz oder bestehende soll erweitert werden
        if self._cards.fits_to(cards_to_merge):
            self._cards += cards_to_merge
        else:
            print("SEC ERROR : Erste Karte aus der eingehende Seq passt nicht")

    def split(self, index):
        # neue sequenz zurückgibt, überschreibt slicing ?
        return self._cards[index:]
    '''
    seq full wenn : 13 karten und alle farben sind gleich
    wenn die erste karte ist 13 und die letzte ist 1 
    ausprobieren mit funktion fits to aus Klasse Card
    '''
    def is_full(self):
        is_full = False
        # wenn die länge 14 ist iteririe von ende bis 14 solange die Folge passt
        if len(self._cards) == 13 and \
                self._cards.first_card().get_value() == 13 and\
                self._cards.last_card().get_value() == 1 and\
                self._cards.first_card().get_color() == self._cards.last_card().get_color():
            for i in range(1, 12):
                if self._cards.get_card_seq(i).get_color() == self._cards.get_card_seq(i + 1).get_color():
                    is_full = True
                else:
                    is_full = False
                    print("Sequence is not full, but firs/last Card is ok ")
                    break
        else:
            print("Sequence is not full, check length, firs/last Card")
        return is_full

    def __str__(self):
        # umwandlung card element zu String
        return "-".join(map(str, self._cards))



if __name__ == "__main__":
    game_cards_hears_1 = []
    game_cards_hears_2 = []
    # Borders are inklusiv
    game_cards_hears_1 = create_cards([1, 8], "hearts")
    game_cards_hears_2 = create_cards([9, 13], "hearts")
    seq_1 = Sequence(game_cards_hears_1)
    seq_2 = Sequence(game_cards_hears_1)



