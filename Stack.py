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
    def __init__(self, sequences, face_down_cards):
        #first list 1 D
        self._sequences = face_down_cards
        #second list 2D
        new_lst = [sequences]
        self._sequences.apppend(sequences)

    def last_sequence(self):
        #in the second dimension are face up cards stored
        return self._sequences[1][-1]

    def is_empty(self):
        "Prueft, ob dieser Stapel leer ist, es also keine offenen Karten mehr gibt."
        return not self._sequences[1]

    def append_sequence(self, sequences):
        self._sequences[1].append(sequences)

    def test_revealcard(self):
        """
        Deckt, wenn moeglich, eine neue Karte von den zugedeckten Karten auf.
        Dafuer muss der Stapel leer sein und es muss noch zugedeckte geben.
        """
        if self.is_empty() and self._face_down_cards:
            #pop saved always the card value !
            self.append_sequence(Sequence([self._face_down_cards.pop()]))

    def test_fullsequence(self):
        if len(self._sequences[1]) == 14:
            self._sequences[1].pop()
            self._sequences.test_revealcard()

    def deal_card(self, card):

        if self._sequences[1] == card:
            self._sequences[1].append(card)
            self._sequences[1].test_fullsequence()
        else:
            #create new sequency
            pass

    def __str__(self):
        stack_str = " ".join(len(self._face_down_cards) * uni_cards['face_down']) + " "
        stack_str += " ".join(map(str, self._sequences))
        return stack_str



