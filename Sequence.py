class Sequence:
    """
     modelliert eine absteigende Sequenz von Karten
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
    print()
    print()
    print()
    print()
