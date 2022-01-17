import random
class AskCard:

    def askNewCard(self):
        print("", end='\n')
        answer = input("Would you like a new card? Y or yes/N or no ",)
        transformedAnswer = answer.upper()

        while (transformedAnswer != "YES" and transformedAnswer != "Y" and transformedAnswer != "NO" and transformedAnswer != "N"):
            print("Not a correct option. Please type yes or no")
            answer = input(" ")
            transformedAnswer = answer.upper()

        if (transformedAnswer == "Y" or transformedAnswer == "YES"):
            return True
        else:
            return False

    def cpuAction(self, total_card_sum):
        global decision
        if total_card_sum == 21:
            decision = 0
        elif total_card_sum > 15 and total_card_sum < 21:
            decision = 0
        elif total_card_sum < 11:
            decision = 1
        else:
            option = random.randint(0, 1)
            if option == 0:
                decision = 0
            else:
                decision = 1
        return decision


