from asker.AskAceValue import AskAceValue
from calculator.CalculateSumList import CalculateListSum
from initialization.CheckValueAndFigure import CheckValueAndFigure
from transform.StringToInt import StringToInt
from winner.Winner import Winner
from initialization.GenerationCards import GenerationCards
from asker.AskCard import AskCard
import time


class RunApplication:

    def __init__(self):
         self.askValue = AskAceValue()
         self.calculateSumList = CalculateListSum()
         self. checkValueAndFigure = CheckValueAndFigure()
         self. stringToInt = StringToInt()
         self. winner = Winner()
         self. generationCard = GenerationCards()
         self. askCard = AskCard()

    def run_application(self):
        '''
        PLAYER CARD GENERATION AND CALCULATION

        '''''

        player_name = input("Welcome to the blackjack app. Please introduce your name ")
        card1_player = self.generationCard.generateCard()
        figure1_player = self.generationCard.generateFigure()
        player_dictionary = self.generationCard.introduceElementsInDictionary(card1_player, figure1_player)
        # generate second card for player-> check first to see if  it is not already there
        card2_player = self.generationCard.generateCard()
        figure2_player = self.generationCard.generateFigure()
        is_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_player, figure2_player,
                                                                                     player_dictionary)
        while is_card_already_present:
            print("Regenerating card")
            card2_player = self.generationCard.generateCard()
            figure2_player = self.generationCard.generateFigure()
            is_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_player, figure2_player,
                                                                                         player_dictionary)
        # add card in dictionary
        self.generationCard.introduceNewCardInDictionary(card2_player, figure2_player, player_dictionary)
        print("Your cards are", end='\n')
        self.generationCard.printPlayerCard(player_dictionary)
        print("", end='\n')
        # check now to see if player wants another card
        want_new_card = self.askCard.askNewCard()
        while want_new_card == True:
            # print("", end='\n')
            # generate temp cards
            temp_card = self.generationCard.generateCard()
            temp_figure = self.generationCard.generateFigure()
            # check in dictionary to see if card exists
            is_temp_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card, temp_figure,
                                                                                              player_dictionary)
            while is_temp_card_already_present:
                print("Regenerating card", end='\n')
                temp_card = self.generationCard.generateCard()
                temp_figure = self.generationCard.generateFigure()
                is_temp_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card,
                                                                                                  temp_figure,
                                                                                                  player_dictionary)
            self.generationCard.introduceNewCardInDictionary(temp_card, temp_figure, player_dictionary)

            self.generationCard.printPlayerCard(player_dictionary)
            want_new_card = self.askCard.askNewCard()
        # put cards into list
        list_cards_player = self.stringToInt.transformStringToIntPlayer(player_dictionary)
        player_sum = self.calculateSumList.calculateSumOfList(list_cards_player, player_name)
        '''
        CPU PART    
        '''

        card1_cpu = self.generationCard.generateCard()
        figure1_cpu = self.generationCard.generateFigure()
        # check to see if card is ok to be generated
        is_cpu_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(card1_cpu, figure1_cpu, player_dictionary)
        while is_cpu_card_already_present:
            print("Regenerating card")
            card1_cpu = self.generationCard.generateCard()
            figure1_cpu = self.generationCard.generateFigure()
            is_cpu_card_already_present = self.checkValueAndFigure.checkIfCardAlreadyPresent(card1_cpu, figure1_cpu, player_dictionary)
        # generate cpu dictionary
        cpu_dictionary = self.generationCard.introduceElementsInDictionary(card1_cpu, figure1_cpu)
        # generate card2 and check to see if it is present in both dictionaries
        card2_cpu = self.generationCard.generateCard()
        figure2_cpu = self.generationCard.generateFigure()
        is_cpu_card2_already_present_in_player_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_cpu, figure2_cpu, player_dictionary)
        is_cpu_card2_already_present_in_cpu_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_cpu, figure2_cpu, cpu_dictionary)
        #we need to check in both sides
        while is_cpu_card2_already_present_in_player_dict or is_cpu_card2_already_present_in_cpu_dict:
            print("Regenerating card", end ='\n')
            card2_cpu = self.generationCard.generateCard()
            figure2_cpu = self.generationCard.generateFigure()
            is_cpu_card2_already_present_in_player_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_cpu, figure2_cpu, player_dictionary)
            is_cpu_card2_already_present_in_cpu_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(card2_cpu, figure2_cpu, cpu_dictionary)
        #put card in dictionary cpu
        self.generationCard.introduceNewCardInDictionary(card2_cpu, figure2_cpu, cpu_dictionary)
        #calculate for cpu sum
        list_card_cpu = self.stringToInt.transformStringToIntComputer_firstPhase(cpu_dictionary)
        cpu_sum_initial = self.calculateSumList.calculateSumOfList(list_card_cpu, "computer")
        #check to see if cpu wants new card
        cpu_wants_new_card = self.askCard.cpuAction(cpu_sum_initial)
        new_sum_cpu = 0
        while cpu_wants_new_card==1:
            #generate new card for cpu
            temp_card_cpu = self.generationCard.generateCard()
            temp_figure_cpu = self.generationCard.generateFigure()
            #check to see if card is ok
            is_cpu_tempCard_already_present_in_player_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card_cpu, temp_figure_cpu, player_dictionary)
            is_cpu_tempCard_already_present_in_cpu_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card_cpu, temp_figure_cpu, cpu_dictionary)
            while is_cpu_tempCard_already_present_in_player_dict or is_cpu_tempCard_already_present_in_cpu_dict:
                print("Regenerating card", end='\n')
                temp_card_cpu = self.generationCard.generateCard()
                temp_figure_cpu = self.generationCard.generateFigure()
                is_cpu_tempCard_already_present_in_player_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card_cpu, temp_figure_cpu, player_dictionary)
                is_cpu_tempCard_already_present_in_cpu_dict = self.checkValueAndFigure.checkIfCardAlreadyPresent(temp_card_cpu, temp_figure_cpu, cpu_dictionary)
            #re-check and see if he wants another card
            self.generationCard.introduceNewCardInDictionary(temp_card_cpu, temp_figure_cpu, cpu_dictionary)
            list_card_cpu = self.stringToInt.transformStringToIntComputer_secondPhase(cpu_dictionary,cpu_sum_initial)
            new_sum_cpu = self.calculateSumList.calculateSumOfList(list_card_cpu, "cpu")
            cpu_wants_new_card = self.askCard.cpuAction(new_sum_cpu)

        #check to see what sum to use for cpu
        if cpu_sum_initial >=new_sum_cpu:
            final_sum_cpu = cpu_sum_initial
        else:
            final_sum_cpu = new_sum_cpu


        '''
        PRINT TO SEE THE WINNER NOW
        '''
        print("FInal cards are")
        time.sleep(1.5)
        print("{} has the following cards: ".format(player_name)); self.generationCard.printPlayerCard(player_dictionary)
        print('\n')
        time.sleep(1.5)
        print("Cpu has the following cards "); self.generationCard.printPlayerCard(cpu_dictionary)
        print ('\n')
        time.sleep(1.5)
        print(" {} has {} ".format(player_name, player_sum))
        print("Cpu has {} ". format(final_sum_cpu))


        result = self.winner.checkWinner(player_sum,final_sum_cpu,list_cards_player, list_card_cpu,player_name)
        time.sleep(2)
        print('\n')
        print(result)









