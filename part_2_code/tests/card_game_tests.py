import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Ace", 1)
        self.card_2 = Card("hearts", 7)
        self.cards = [self.card_1, self.card_2] #do i need this part for 3rd test?
        self.cardGame = CardGame ()

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card_1))

    def test_highest_card(self):
        self.assertEqual(self.card_2,self.cardGame.highest_card(self.card_1, self.card_2))

    

    def test_cards_total(self):
        self.assertEqual('You have a total of 8.', self.cardGame.cards_total(self.cards))


        



