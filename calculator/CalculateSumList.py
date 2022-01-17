class CalculateListSum:

    def calculateSumOfList(self, list_values, player_name):
        sum=0
        for i in range(0, len(list_values)):
            sum+=list_values[i]
        return sum

