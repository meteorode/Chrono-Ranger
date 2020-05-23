# chrono_cross.py

# Themes:
#   1.  A game about history and predestination.
#   2.  Leading/witnessing humanity to different destinies by triggering/changing history events.

# Features:
#   1.  Shuffle/Play your own deck into linear history events.
#   2.  Click an event card to resolve it
#   3.  Roll dice to resolve events.
#   4.  While resolved a card, check special match-3 rules(i.e, [Char, Location, Story] with same color
#       would trigger new effects).

import random
import json
import time
from datetime import date, datetime
from random import *
from pathlib import Path
from collections import Counter

# Define Colors here.
COLOR_RED = 0
COLOR_GREEN = 1
COLOR_BLUE = 2
COLOR_YELLOW = 3
COLOR_WHITE = 4
COLOR_BLACK = 5

class card: # Cards are heroes, events, locations, treasures, etc. Cards have color used for match-3.
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.color = COLOR_RED

class deck: # Deck is an array of [Cards], will implement some features like draw, discard, remove, etc.
    def __init__(self): 
        self.all = []   # All cards in deck
        self.hands = [] # Hands also equal to battleCommander's hands
        self.draw_pile = [] # Cards used for drawing.
        self.discard_pile = [] # Cards discarded came here.
        self.trash = [] # Cards temporarily removed from battle came here.

    def draw(self, draw_number): # Randomly add [draw_number] cards from draw pile.
        pass    # _TO_BE_CONTINUED_

    def add_card(self, card): # Add a specific card to hands.
        pass    # _TO_BE_CONTINUED_

    def discard_card(self, card): # Discard a specific card to discard pile.
        pass    # _TO_BE_CONTINUED_

    def trash_card(self, card): # temporarily remove a card from battle.
        pass    # _TO_BE_CONTINUED_

def main(): # Main loop about what a player can do in this game.
    pass

if __name__ == "__main__":
    main()
