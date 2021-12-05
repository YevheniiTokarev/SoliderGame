
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


class Sequence(Card):
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

# how to use self._cards.last_card.get_value()
    def fits_to(self, cards):
        print("last", self.last_card().get_value())
        print("first", cards.first_card().get_value())
        return self.last_card().get_value() - 1 == cards.first_card().get_value()

    def merge(self, cards_to_merge):
        # fits to nötig ??
        # neue sequenz oder bestehende soll erweitert werden
        if self.fits_to(cards_to_merge):
            self._cards += cards_to_merge
        else:
            print("SEC ERROR : Erste Karte aus der eingehende Seq passt nicht")

    def split(self, index):
        # neue sequenz zurückgibt, überschreibt slicing --> Nein
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
                self.first_card().get_value() == 13 and\
                self.last_card().get_value() == 1 and\
                self.first_card().get_color() == self.last_card().get_color():
            for i in range(1, 12):
                if self.get_card_seq(i).get_color() == self.get_card_seq(i + 1).get_color():
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


class Stack(Sequence):
        """
           Ein Stapel von Sequenzen. Diese Klasse modelliert die einzelnen Stapel des Spiels.
           Neben den Sequenzen, welche den aufgedeckten Karten entsprechen, merkt sich ein Stapel noch die umgedrehten/verdeckten Karten.
        """

        '''Konstruktor erwartet eine Card-Instanz, welche die bereits sichtbare Karte reprasentiert
        und eine Liste von Card-Instanzen, welche die noch verdeckten Karten darstellen.'''
        def __init__(self, face_down_cards, card_open):
            new_sequence = [card_open]
            # create a new sequence
            self._sequences.apppend(Sequence(new_sequence))
            self._face_down_cards = face_down_cards

        def last_sequence(self):
            return self._sequences[-1]

        def is_empty(self):
            return not self._sequences[0]

        # todo check ob value color ok sind, benutze funktionen von anderen Klassen
        def append_sequence(self, sequences):
            self._sequences.append(sequences)

        def test_revealcard(self):
            """
            Deckt, wenn moeglich, eine neue Karte von den zugedeckten Karten auf.
            Dafuer muss der Stapel leer sein und es muss noch zugedeckte geben.
            """
            if self.is_empty() and len(self._face_down_cards) != 0:
                new_sequence = self._face_down_cards.pop()
                self._sequences.apppend(Sequence(new_sequence))
            else:
                print("Stack ist komplett leer! Karte kann nicht aufgedeckt werden ")


        def test_full_sequence(self):
            if self.last_sequence().is_full():
                self._sequences.pop()
                self.test_revealcard()
            else:
                print("Sequence is not full ...")


        def deal_card(self, card):
            if self.last_sequence().last_card().fits_to(card):
                self.last_sequence().append_card(card)
                self.test_full_sequence()
            else:
                print("Karte passt nicht, wird neue Seq erzeugt")
                new_sequence = [card]
                self._sequences.apppend(Sequence(new_sequence))

        def __str__(self):
            stack_str = " ".join(len(self._face_down_cards) * uni_cards['face_down']) + " "
            stack_str += " ".join(map(str, self._sequences))
            return stack_str


if __name__ == "__main__":
    card_1 = Card(2, "hearts")
    card_2 = Card(3, "hearts")
    card_3 = Card
    game_cards_hears_1 = []
    game_cards_hears_2 = []
    # Borders are inklusiv
    game_cards_hears_1 = create_cards([1, 8], "hearts")
    game_cards_hears_2 = create_cards([9, 13], "hearts")

    seq_1 = Sequence(game_cards_hears_1)
    print("Seq 1 first bevor: ", seq_1.first_card().get_value())
    print("Seq 1 first bevor: ", seq_1.last_card().get_value())
    #TODo : funktion anpassen so dass es fits to aus Klasse Card ausgeführt wird
    seq_1.append_card(card_1)
    print("Seq 1 first after: ", seq_1.first_card().get_value())
    print("Seq 1 first after: ", seq_1.last_card().get_value())

    print(seq_1.split(5))
    print(seq_1)

    seq_2 = Sequence(game_cards_hears_2)
    print("Seq 2 first bevor: ", seq_2.first_card().get_value())
    print("Seq 2 last bevor: ", seq_2.last_card().get_value())
    seq_2.append_card(card_2)
    print("Seq 2 first after: ", seq_2.first_card().get_value())
    print("Seq 2 last after: ", seq_2.last_card().get_value())

    seq_1.merge(seq_2)
    print(seq_1)

