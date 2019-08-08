from abc import ABC, abstractmethod
from itertools import combinations
from random import choice


class Card(ABC):
    @abstractmethod
    def __init__(self, color, number, shade):
        self.color = color
        self.number = number
        self.shade = shade

    def __str__(self):
        return "[Card: {} : {} : {}]".format(self.color, self.number, self.shade)


class OvalCard(Card):
    def __init__(self, color, number, shade):
        self.shape = "Oval"
        super().__init__(color, number, shade)


class SquiggleCard(Card):
    def __init__(self, color, number, shade):
        self.shape = "Squiggle"
        super().__init__(color, number, shade)


class DiamondCard(Card):
    def __init__(self, color, number, shade):
        self.shape = "Diamond"
        super().__init__(color, number, shade)


class CardFactory():
    available_cards = [SquiggleCard, OvalCard, DiamondCard]
    available_colors = ["red", "purple", "green"]
    available_numbers = [1, 2, 3]
    available_shades = ["solid", "striped", "outlined"]

    @staticmethod
    def create_card():
        color = choice(CardFactory.available_colors)
        number = choice(CardFactory.available_numbers)
        shade = choice(CardFactory.available_shades)
        return choice(CardFactory.available_cards)(color, number, shade)


def is_same_type(cards):
    first_card_type = type(cards[0])
    return all(type(x) == first_card_type for x in cards)


def is_different_type(cards):
    cards_set = set([type(card) for card in cards])
    return len(cards) == len(cards_set)


def is_same_color(cards):
    first_card_color = cards[0].color
    return all(card.color == first_card_color for card in cards)


def is_different_color(cards):
    cards_set = set([card.color for card in cards])
    return len(cards) == len(cards_set)


def is_same_number(cards):
    first_card_number = cards[0].number
    return all(card.number == first_card_number for card in cards)


def is_different_number(cards):
    cards_set = set([card.number for card in cards])
    return len(cards) == len(cards_set)


def is_same_shade(cards):
    first_card_shade = cards[0].shade
    return all(card.shade == first_card_shade for card in cards)


def is_different_shade(cards):
    cards_set = set([card.shade for card in cards])
    return len(cards) == len(cards_set)


def is_set(cards):
    return (is_same_type(cards) or is_different_type(cards)) and \
           (is_same_color(cards) or is_different_color(cards)) and \
           (is_same_number(cards) or is_different_number(cards)) and \
           (is_same_shade(cards) or is_different_shade(cards))


class SetGameBoard():
    def __init__(self):
        self.cards = []
        self.new_game()

    def new_game(self):
        self.cards = [CardFactory.create_card() for x in range(12)]

    def find_sets(self):
        card_combinations = combinations(self.cards, 3)
        sets = [cards for cards in card_combinations if is_set(cards)]
        return sets
