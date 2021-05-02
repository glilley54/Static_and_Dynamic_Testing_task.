import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Ace", 1)

    def test_card_has_suit(self):
        self.assertEqual("Ace",self.card_1.suit)

    def test_highest_card(self):
        self.assertEqual(8,8,4)    
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 7", (cards_total(7))


        



