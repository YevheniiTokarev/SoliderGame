class Sequence:
    """
     modelliert eine absteigende Sequenz von Karten
    """

    def __init__(self, cards):
        self._cards = cards

    def first_card(self):
        return self._cards[0]

    def last_card(self):
        return self._cards[-1]

    #ToDo check Attribut card_in, bzw ob carten zu einander passen
    #Todo prüfe ob input card dem Standart entspricht lst, values grenzen
    def append_card(self, card):
        return self._cards.append(card)
#first card is
    def fits_in(self, cards):
        return int(self._cards[-1]) == int(cards.first_card()) - 1

    def merge(self, cards_to_merge):
        self._cards += cards_to_merge

    def split(self, position):
        # neue sequenz ?
        return self._cards[position:]
# now only full by value , @TODO full color check
    def is_full(self):
        print("the Length is: ", len(self._cards))
        return len(self._cards) == 14

    def __str__(self):
        #umwandlung card element zu String
        return "-".join(map(str, self._cards))

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9, 10]
    l_2 = [11,12,13]
    s = Sequence(l)
    print(s.first_card())
    print(s.last_card())
    print(s.is_full())
    sec_card = Sequence(l_2)
    print(s.fits_in(sec_card))

