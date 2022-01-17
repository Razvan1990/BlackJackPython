class Winner:
    def checkWinner(self, sum_player, sum_cpu, list_card_player, list_card_cpu, name_player):
        # player winnings
        if sum_player == sum_cpu == 21 and len(list_card_player) == 2:
            return name_player + "has won. BlackJack"
        elif sum_player > sum_cpu and sum_player == 21:
            return name_player + "has won. You have 21"
        elif sum_player > sum_cpu and sum_player < 21:
            return name_player + "has won. You have a better score than your opponent"
        elif sum_player < 22 and sum_cpu > 21:
            return name_player + "has won. Opponent has busted"

        #equality
        elif sum_player==sum_cpu==21 and len(list_card_player) == len(list_card_cpu) ==2:
            return "Wow. It is a draw! You both have blackjack"
        elif sum_player==sum_cpu and sum_player <21:
            return "Draw . You both have ", sum_player, "!"
        elif sum_player>21 and sum_cpu >21:
            return "Haha. You both have busted"

        #computer winnings
        if sum_player == sum_cpu == 21 and len(list_card_cpu) == 2:
            return "Cpu has won. BlackJack"
        elif sum_player < sum_cpu and sum_cpu == 21:
            return  "Cpu has won. He has 21"
        elif sum_player < sum_cpu and sum_cpu < 21:
            return  "Cpu has won. Has a better score than you"
        elif sum_player >21 and sum_cpu < 22:
            return "Cpu has won. "+name_player+ " has busted"
