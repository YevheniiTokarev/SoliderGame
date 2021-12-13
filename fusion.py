
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
        # lieber while solange nicht richtig
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
    def fits_to(self, drop_card, value_only=False):
        if value_only:
            return self._value - 1 == drop_card.get_value() and self._color != drop_card.get_color()
        else:
            return self._value - 1 == drop_card.get_value() and self._color == drop_card.get_color()

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
#slicing?! function ?
    def get_card_seq(self, index):
        return self._cards[index]

    # ToDo check Attribut card_in, bzw ob carten zu einander passen
    # Todo prüfe ob input card dem Standart entspricht lst, values grenzen
    #wenn es nur für start austeilung benötigt wird , dann obere Anmerkungen sind  unwichitg ..
    def append_card(self, card):
        self._cards.append(card)

# how to use self._cards.last_card.get_value()
    #schreibe separat 2 funktionen fits to value fits to color fit_value().fitcolor()...
    def fits_to(self, cards, value_only=False):
        print("last", self.last_card().get_value())
        print("first", cards.first_card().get_value())
        return self.last_card().fits_to(cards.first_card(), value_only=value_only)

    def merge(self, cards_to_merge):
        self._cards += cards_to_merge

    def split(self, index):
        splitted = Sequence(self._cards[index:])
        self._cards[:] = self._cards[:index]
        return splitted
        #if splitted.is_full():
         #   raise SpiderSolitaireError("Splitted an empty Sequence")

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

    def is_empty(self):
        return not self._cards

    def __str__(self):
        # umwandlung card element zu String
        return "-".join(map(str, self._cards))

    def __iter__(self):
        for card in self._cards:
            yield card


class Stack(Sequence):
        """
           Ein Stapel von Sequenzen. Diese Klasse modelliert die einzelnen Stapel des Spiels.
           Neben den Sequenzen, welche den aufgedeckten Karten entsprechen, merkt sich ein Stapel noch die umgedrehten/verdeckten Karten.
        """

        '''Konstruktor erwartet eine Card-Instanz, welche die bereits sichtbare Karte reprasentiert
        und eine Liste von Card-Instanzen, welche die noch verdeckten Karten darstellen.
        Aufbau --> [seq_face_down, Seq_face_open]'''
        def __init__(self, face_down_cards, card_open):
            self._sequences = Sequence([card_open])
            self._face_down_cards = face_down_cards

        def last_sequence(self):
            return self._sequences[-1]

        def is_empty(self):
            return not self._sequences

        def append_sequence(self, sequence):
            self._sequences.append(sequence)

        def del_last_sequece(self):
            self._sequences.pop()

        def test_revealcard(self):
            """
            Deckt, wenn moeglich, eine neue Karte von den zugedeckten Karten auf.
            Dafuer muss der Stapel leer sein und es muss noch zugedeckte geben.
            [ seq_face_down, seq_up_1, seq_up_2 ..] if seq_face_down not empty and seq_up_1 is empty  and full stack not empty
            """
            if self.is_empty() and self._face_down_cards:
                self.append_sequence((Sequence[self._face_down_cards.pop()]))
            else:
                print("Stack ist komplett leer! Karte kann nicht aufgedeckt werden ")


        def test_full_sequence(self):
            if self.last_sequence().is_full():
                self._sequences.pop()
                self.test_revealcard()
            else:
                print("Sequence is not full ...")


        def deal_card(self, card):
            last_card = self.last_sequence().last_card()
            if card.fits_to(last_card):
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

#use generator, We can use more than one yield statement in a generator.
        def __iter__(self):
            for i in self._self._sequences:
                for j in i:
                    yield j


class SpiderSolitaire(Stack):
    def __init__(self, stacks, stack2deal):
        self._stacks = stacks
        # Liste von Card-Instanzen, der noch zu verteilenden Karten,
        self._stack2deal = Sequence(stack2deal)

    def is_empty_stacks(self):
        empty = False
        for i in self._stacks:
            #i[0] sind face down cards
            if len(i[0]) == 0:
                empty = True
                break
        return empty

    def deal(self):
        if len(self._stack2deal) != 0 and self.is_empty_stacks():
            # run into each stack
            for i in self._stacks:
                # run into each seq in the stack
                for j in i:
                    j.append(self._stack2deal.pop())
                    if len(self._stack2deal) == 0:
                        print("Stack2Deal empty")
                        break
        else:
            print("Stack2Deal is leer oder Karte nicht aufgedeckt ist!")

    def __str__(self):
        res = ""
        for i, stack in enumerate(self.stacks):
            res += str(i) + "" + str(stack) + "\n"
        res += "#" * 80 + "\n"
        return res



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

