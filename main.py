import  random


# Anfangskonfiguration des Spiels
def initialize():

    # Alle/Verdeckte Karten --> 104 --> 8*13
    stack2deal = []
    for _ in range(0, 8):
        stack2deal += ([x+1 for x in range(0,13)])
    print(stack2deal)
    # Unverdeckte Karten 10 Stück am anfang leer, ausfüllen beim aufteilen
    stacks = {}
    #Anzahl verdeckte Karten pro Stapel, am Anfang leer da noch nicht verteilt
    cards2deal_perstack = []
    return stacks,stack2deal,cards2deal_perstack

def deal(stacks, stack2deal, cards2deal_perstack):
    # Fühle 10 Stapeln mit verdeckten Karten
    counter_fivestack = 4
    card_pick = 52
    card_herz = 52
    for run in range(0, 10):
        each_stack = []
        for run_2 in range(0, 4):
            card = random.choice(stack2deal)
            stack2deal.remove(card)
            each_stack.append(card)
        cards2deal_perstack.append(each_stack)
        # erste 4 Stapeln haben 5 verdeckte Karten
        if counter_fivestack != 0:
            card = random.choice(stack2deal)
            stack2deal.remove(card)
            cards2deal_perstack[run].append(card)
            counter_fivestack -= 1
        # Erstelle List mit unverdeckten karten
        card_value = random.choice(stack2deal)
        stack2deal.remove(card_value)
        card_color = random.randint(0, 1)
        # Pick/schwarz = 0 Herz/rot =1, max für jede 52
        if card_color == 0:
            card_color = "Pick"
            card_pick -= 1
        else:
            card_color = "Herz"
            card_herz -= 1
        open_card = {card_color: card_value}
        cards2deal_perstack[run].append(open_card)

    print(cards2deal_perstack)

#@ToDo Itegration in deal?? an welcher Stelle wird benutzt
def test_fullsequence(stack_sequence):
    # Volle Stapel
    target_sequence = [x+1 for x in range(0,13)]

    return set(stack_sequence) == set(target_sequence)

def test_revealcard(stack_sequence):

    # Input ist eine Stapel, wenn letzte Element aus der Stapel kein dict ist
    # gibt es keine unverdeckte Karte an der Stelle
    return isinstance(stack_sequence[-1], dict)



if __name__ == '__main__':

    stacks, stack2deal, cards2deal_perstack = initialize()
    deal(stacks, stack2deal, cards2deal_perstack)