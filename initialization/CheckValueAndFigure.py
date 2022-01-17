from multidict import MultiDict
class CheckValueAndFigure:

    #method to check if card already exists in dictionary
    def checkIfCardAlreadyPresent(self,card, figure,  multidictionary):
        if (card, figure) in multidictionary.items():
            return True
        else:
            return False








