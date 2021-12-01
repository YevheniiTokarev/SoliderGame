import Sequence
import Card

class Stack:
    """
       Ein Stapel von Sequenzen. Diese Klasse modelliert die einzelnen Stapel des Spiels.
       Neben den Sequenzen, welche den aufgedeckten Karten entsprechen, merkt sich ein Stapel noch die umgedrehten/verdeckten Karten.
       umgedrehte kartes sind immer 1 element !  [[gedeckte][ungedekte]]
       """
    '''Konstruktor erwartet eine Card-Instanz, welche die bereits sichtbare Karte reprasentiert
    und eine Liste von Card-Instanzen, welche die noch verdeckten Karten darstellen.'''
    def __init__(self, face_down_cards, card_open):
        #first list 1 D
        self._sequences = []
        self._sequences.apppend(face_down_cards)
        #second list 2D
        new_lst = [card_open]
        self._sequences.apppend(card_open)

    def last_sequence(self):
        #in the second dimension are face up cards stored [[down], [up]]
        return self._sequences[1]

    def is_empty(self):
        "Prueft, ob dieser Stapel leer ist, es also keine offenen Karten mehr gibt."
        return not self._sequences[1]
#todo check ob value color ok sind
    def append_sequence(self, sequences):
        self._sequences[1].append(sequences)

    def test_revealcard(self):
        """
        Deckt, wenn moeglich, eine neue Karte von den zugedeckten Karten auf.
        Dafuer muss der Stapel leer sein und es muss noch zugedeckte geben.
        """
        if len(self._sequences[0]) > 0 and len(self._sequences[1]) == 0:
            self._sequences[1].append(self._sequences[0][-1])
        elif len(self._sequences[0] == 0):
            print("Halter ist leer")
        else:
            print("Etwas schief gelaufen")
# only by value but not by color
    def test_fullsequence(self):
        if len(self._sequences[1]) == 14:
            self._sequences[1].pop()
            self._sequences.test_revealcard()
        else:
            print("NOT FULL")

    def deal_card(self, card):

        if self._sequences[1] == card[1]:
            self._sequences[1].append(card)
            self._sequences[1].test_fullsequence()
        else:
            #create new sequency
            pass

    def __str__(self):
        stack_str = " ".join(len(self._face_down_cards) * uni_cards['face_down']) + " "
        stack_str += " ".join(map(str, self._sequences))
        return stack_str


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9, 10]
    m = Stack([1,2,3], 5)
