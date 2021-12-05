import Sequence
import Card

class Stack:
    """
       Ein Stapel von Sequenzen. Diese Klasse modelliert die einzelnen Stapel des Spiels.
       Neben den Sequenzen, welche den aufgedeckten Karten entsprechen, merkt sich ein Stapel noch die umgedrehten/verdeckten Karten.
    """

    '''Konstruktor erwartet eine Card-Instanz, welche die bereits sichtbare Karte reprasentiert
    und eine Liste von Card-Instanzen, welche die noch verdeckten Karten darstellen.'''
    def __init__(self, face_down_cards, card_open):
        #first list 1 D
        new_sequence = [card_open]
        self._sequences.apppend(new_sequence)
        self._face_down_cards = face_down_cards


    def last_sequence(self):
        #in the second dimension are face up cards stored [[down], [up]]
        return self._sequences[1]

    def is_empty(self):
        # wenn die zweite Liste leer ist --> keine offene Karten
        return not self._sequences[1]
#todo check ob value color ok sind, benutze funktionen von anderen Klassen
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
        @TODO !!!!!!!!!!!
        '''seq_number = len(self._sequences[1])
        if seq_number > 0:
            for i in self._sequences[1]:
                 '''
        if len(self._sequences[1]) == 14:
            self._sequences[1].pop()
            self._sequences.test_revealcard()
        else:
            print("NOT FULL")

    def deal_card(self, card):
        # [[nS1, nS2, nS3],[[S1,S2,S3],[S1,S2,S3]],]
        # opencards-->last seq-->last card-->value of card
        if self._sequences[1][-1][-1][-1] == card[1]:
            self._sequences[1][-1].append(card)
            self._sequences[1].test_fullsequence()
        else:
            self._sequences[1].append(card)
            print("New card was added")



    def __str__(self):
        stack_str = " ".join(len(self._face_down_cards) * uni_cards['face_down']) + " "
        stack_str += " ".join(map(str, self._sequences))
        return stack_str


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9, 10]
    m = Stack([1,2,3], 5)
