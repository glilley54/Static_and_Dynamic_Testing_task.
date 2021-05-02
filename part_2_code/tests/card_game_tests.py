import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Ace", 1)
        self.card_2 = Card("hearts", 7)
        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace(self):
        self.assertEqual("Ace", self.card_1.suit)

    def test_highest_card(self):
        self.assertEqual(8,8,2)    
    
    def test_cards_total(self):

        self.assertEqual("You have a total of 8",self.cards)


        



