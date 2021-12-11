import random

class SpiderSolitaire:
    """
    Klasse, die das ganze Spielfeld an sich verwaltet.
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
    """


    def __init__(self, stacks, stack2deal):
        self._stacks = stacks
        # Liste von Card-Instanzen, der noch zu verteilenden Karten,
        self._stack2deal = stack2deal

    def deal(self):


    def __str__(self):
        res = ""
        for i, stack in enumerate(self.stacks):
            res += str(i) + "" + str(stack) + "\n"
        res += "#"*80 + "\n"
        return res



if __name__ =="main":
    random.seed(83273884)
    ss = SpiderSolitaire()
    for _ in range(5):
        ss.deal
    print(ss)
