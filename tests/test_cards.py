import unittest

import war

from war import Cards
from war.Cards import *

class TestCards(unittest.TestCase):

    def test_initial_deck_52(self):
        deck = Deck()
        self.assertEqual(deck.count,52)

    def test_invalid_rank(self):
        self.assertRaises(ValueError, Card,1,"Club")
        self.assertRaises(ValueError, Card,15,"Club")

    def test_invalid_suit(self):
        self.assertRaises(ValueError, Card,2,"flibertyjibit")

    def test_card_equal(self):
        card1 = Card(5,"Heart")
        card2 = Card(5,"Heart")
        self.assertEqual(card1,card2)

    def test_card_ne(self):
        card1 = Card(5,"Heart")
        card2 = Card(6,"Heart")
        self.assertNotEqual(card1,card2,"Different ranks shouldn't be equal")
        card1 = Card(5,"Heart")
        card2 = Card(5,"Club")
        self.assertNotEqual(card1,card2,"Different suits shouldn't be equal")
        
    def test_draw(self):
        deck = Deck()

        card = deck.draw()

        self.assertEqual(deck.count,51,"Drawing a card should reduce the deck count")

        for c in deck._cards:
            self.assertNotEqual(card,c,"Card shouldn't be in a deck after drawing")

    def test_multidraw(self):
        deck = Deck()
        card_count = 5
        cards = deck.draw_multiple(card_count)

        self.assertEqual(deck.count,52-card_count,"Deck should be reduced by the correct number of cards")
        self.assertEqual(len(cards),card_count, "You should get back the correct number of cards")

    def test_bad_draw(self):
        deck = Deck(existing_cards=[])
        self.assertRaises(ValueError,deck.draw)
        self.assertRaises(ValueError,deck.draw_multiple,5)

    
