from multidict import MultiDict
from asker.AskAceValue import AskAceValue


class StringToInt:

    def __init__(self):
        self.askValue = AskAceValue()

    def introduceKeysIntoList(self, multidictionary):
        cards = []
        for x in multidictionary.keys():
            cards.append(x)

        return cards

    def transformStringToIntPlayer(self, multidictionary):
        list_string_cards = self.introduceKeysIntoList(multidictionary)
        cards_int = []
        card = 0
        for i in range(0, len(list_string_cards)):
            if list_string_cards[i] == "2":
                card = 2;
                cards_int.append(card)
            elif list_string_cards[i] == "3":
                card = 3;
                cards_int.append(card)
            elif list_string_cards[i] == "4":
                card = 4;
                cards_int.append(card)
            elif list_string_cards[i] == "5":
                card = 5;
                cards_int.append(card)
            elif list_string_cards[i] == "6":
                card = 6;
                cards_int.append(card)
            elif list_string_cards[i] == "7":
                card = 7;
                cards_int.append(card)
            elif list_string_cards[i] == "8":
                card = 8;
                cards_int.append(card)
            elif list_string_cards[i] == "9":
                card = 9;
                cards_int.append(card)
            elif list_string_cards[i] == "A":
                card = self.askValue.askOfAceValuePlayer()
                cards_int.append(card)
            else:
                card = 10;
                cards_int.append(card)
        return cards_int

    def transformStringToIntComputer_firstPhase(self, multidictionary):
        list_string_cards = self.introduceKeysIntoList(multidictionary)
        cards_int = []
        card = 0
        for i in range(0, len(list_string_cards)):
            if list_string_cards[i] == "2":
                card = 2
                cards_int.append(card)
            elif list_string_cards[i] == "3":
                card = 3
                cards_int.append(card)
            elif list_string_cards[i] == "4":
                card = 4
                cards_int.append(card)
            elif list_string_cards[i] == "5":
                card = 5
                cards_int.append(card)
            elif list_string_cards[i] == "6":
                card = 6
                cards_int.append(card)
            elif list_string_cards[i] == "7":
                card = 7
                cards_int.append(card)
            elif list_string_cards[i] == "8":
                card = 8
                cards_int.append(card)
            elif list_string_cards[i] == "9":
                card = 9
                cards_int.append(card)
            elif list_string_cards[i] == "A":
                card = self.askValue.setInitialAceValueForComputer(list_string_cards)
                cards_int.append(card)
            else:
                card = 10
                cards_int.append(card)
        return cards_int

    def transformStringToIntComputer_secondPhase(self, multidictionary, sum_cards):
        list_string_cards = self.introduceKeysIntoList(multidictionary)
        cards_int = []
        global card
        for i in range(0, len(list_string_cards)):
            if list_string_cards[i] == "2":
                card = 2
                cards_int.append(card)
            elif list_string_cards[i] == "3":
                card = 3
                cards_int.append(card)
            elif list_string_cards[i] == "4":
                card = 4
                cards_int.append(card)
            elif list_string_cards[i] == "5":
                card = 5
                cards_int.append(card)
            elif list_string_cards[i] == "6":
                card = 6
                cards_int.append(card)
            elif list_string_cards[i] == "7":
                card = 7
                cards_int.append(card)
            elif list_string_cards[i] == "8":
                card = 8
                cards_int.append(card)
            elif list_string_cards[i] == "9":
                card = 9
                cards_int.append(card)
            elif list_string_cards[i] == "A":
                card = self.askValue.setRestAceValueForComputer(sum_cards, list_string_cards)
                cards_int.append(card)
            else:
                card = 10
                cards_int.append(card)
        return cards_int
