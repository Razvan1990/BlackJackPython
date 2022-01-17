import unittest
from runner.RunApplication import RunApplication
from transform.StringToInt import StringToInt
from winner.Winner import Winner
from multidict import MultiDict
from calculator.CalculateSumList import CalculateListSum


class MyTestCase(unittest.TestCase):
    runnner = RunApplication()
    winner = Winner()
    transformer = StringToInt()
    calculate = CalculateListSum()
    def simple_test(self, a, b):
        return a+b
    def test_something(self):
        self.assertEqual(self.simple_test(3,2),5, "The test is not correct")# add assertion here
    def test_negative_2(self):
        self.assertEqual(self.simple_test(10, 10),19, "The test is not correct")
    def test_check_winner(self):

        dict1 = {"8":"frunza","6":"inima","4":"trefla"};dict2 = {"4":"caro","2":"trefla","5":"frunza"}
        list1_integer = self.transformer.transformStringToIntPlayer(dict1)
        list2_integer = self.transformer.transformStringToIntPlayer(dict2)
        score_player1 = self.calculate.calculateSumOfList(list1_integer,"Messi")
        score_player2 = self.calculate.calculateSumOfList(list2_integer,"Ronaldo")
        self.assertGreater(score_player1,score_player2,"The test is not correct cause {} has a bigger score than {} ".format(score_player1, score_player2))
        self.assertTrue(self.winner.checkWinner(score_player1, score_player2, list1_integer, list2_integer,"Messi")=="Messihas won. You have a better score than your opponent","Not the correct answer")



if __name__ == '__main__':
    unittest.main()
