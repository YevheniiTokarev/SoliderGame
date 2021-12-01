import random

#@TODO !!!!!!!!!!!!!!!!!!!!  check  was Konstruktor erwartet
n = [i for i in range(14) if i != 11]
uni_cards = {
    'hearts': {v+1: chr(127153 + n[v]) for v in range(13)},
    'spades': {v+1: chr(127137 + n[v]) for v in range(13)},
    'face_down': chr(127136)
}


class Card:
    """
    Eine einzelne Spielkarte, die Informationen bzgl Kartenwert und -Farbe speichert.
    """
    def __init__(self, value, color):
        self._value = value
        self._color = color
        #@ToDo counter for max number of card for safety ...
        if self._value < 1 or self._value > 13:
            raise Exception("The card Value is false")
        if self._color != "hearts" and self._color != "spades":
            raise Exception("The color of card is false")

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def set_value(self, value):
        self._value = value

    def set_color(self, color):
        self._color = color
# 2D Liste wird benutzt für als Halter für die Karten  lst_1 0 farbe und lst_2 für value

    def __str__(self):
        return uni_cards[self.get_color()][self.get_value()]

    def fits_to(self, card):
        # @ToDo color check now it is only value check
        #value_only = False
        return int(self._value) == int(card.get_value()) - 1


class Sequence:
    """
    Diese Klasse modelliert eine absteigende Sequenz von Karten
    """

    def __init__(self, cards_list):
        self._cards = cards_list

    def first_card(self):
        return self._cards[0]

    def last_card(self):
        return self._cards[-1]

    #ToDo check Attribut card_in
    #Todo prüfe ob input card dem Standart entspricht lst, values grenzen
    def append_card(self, card):
        return self._cards.append(card)

    def fits_in(self, cards):
        return int(self._cards[-1]) == int(cards.first_card()) - 1

    def merge(self, cards_to_merge):
        self._cards += cards_to_merge

    def split(self, position):
        return self._cards[position:]

    def is_full(self):
        print("the Length is: ", len(self._cards))
        return len(self._cards) == 14
'''
    def __str__(self):
        #umwandlung card element zu String
        return "-".join(map(str, self._cards))
'''
#Stack (Stapel von Sequenzen) beschreibt


class SpiderSolitaire:
    """
    Klasse, die das ganze Spielfeld an sich verwaltet.
    """
    def __init__(self):

        #Start Aufstellung 52 Herz und 52 Pcick
        self._stack2deal = 4*[Card(value, color) for value in range(1, 14) for color in ["hearts", "spades"]]

        #change in the order of list item --> Mische Karten
        random.shuffle(self._stack2deal)

        # Anzahl Verdeckte karten pro Spiel
        cards2deal_perstack = [5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
        # Es werden 10 Stapel erzeugt und in self._stacks gespeichert.
        # Jeder Stapel bekommt hierbei die entsprechende Anzahl verdeckter Karten und die eine aufgedeckte Karte uebergeben.
        self.stacks = []
        #10 Stapeln
        for k in range(10):
            face_down_cards = [self._stack2deal.pop() for _ in range(cards2deal_perstack[k])]
            self._stacks.append(Stack(self._stack2deal.pop(), face_down_cards))

    def __str__(self):
        res = ""
        for i, stack in enumerate(self.stacks):
            res += str(i) + "" + str(stack) + "\n"
        res += "#"*80 + "\n"
        return res

    def deal(self):

        if  len(self._stack2deal) != 0 and is_empty():


if __name__ =="main":
    random.seed(83273884)
    ss = SpiderSolitaire()
    for _ in range(5):
        ss.deal
    print(ss)
