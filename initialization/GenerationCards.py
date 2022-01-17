from multidict import MultiDict
from initialization.Constants import Constants
import random



class GenerationCards:

      def __init__(self):
          self.constants = Constants()

      def generateCard(self):
          generated_card = int(random.randint(0, len(self.constants.cards)-1))
          return self.constants.cards[generated_card]

      def generateFigure(self):
          generate_figure = int(random.randint(0, len(self.constants.figures)-1))
          return self.constants.figures[generate_figure]

      def introduceElementsInDictionary(self, card, figure):
           my_multi =MultiDict()
           my_multi.add(card, figure)
           return my_multi


      def introduceNewCardInDictionary(self, card, figure, dictionary):
          dictionary.add(card, figure)

      def printPlayerCard(self, dictionary):
          for x, y in dictionary.items():
              print("[",x," ",y,"]", end ="")






