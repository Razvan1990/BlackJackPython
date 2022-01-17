import random


class AskAceValue:

    def askOfAceValuePlayer(self):
        print("", end='\n')
        answer = int(input("What value would you like your ace to be ? 1 or 11"))
        while (answer != 1 and answer != 11):
                print("Not a correct value. Please introduce the correct value for ace")
                answer = int(input(""))
        # we will use this in the method to transform the string cards into int values
        return answer

    def setRestAceValueForComputer(self,total_card_sum, card_list):
            global ace_value
            if total_card_sum < 11 and len(card_list)<4:
                ace_value = 11
                return ace_value
            elif (total_card_sum > 15 and total_card_sum < 20) and len(card_list)>=3:
                ace_value = 1
                return ace_value
            else:
                option = random.randint(0, 1)
                if option == 0:
                    ace_value = 1
                elif option == 1:
                    ace_value = 11
            return ace_value


    def setInitialAceValueForComputer(self,card_list):
        ace_value =0
        for i in range(0, len(card_list)):
            if card_list[i]=="K" or card_list[i]=="Q"or card_list[i]=="J" or card_list[i]=="10" or card_list[i]=="9" or card_list[i]=="8":
                ace_value =11
                return ace_value
            else:
                option = random.randint(0,1)
                if option==0:
                    ace_value =1
                else:
                    ace_value=11
        return ace_value






