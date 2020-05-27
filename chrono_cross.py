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

# Define Choronauts' class here.
CLASS_CIVILIAN = 0

# Define history ages here.
STONE_AGE = 0 # (? - c.3000 BCE)
BRONZE_AGE = 1 # (c.3000 BCE – c.1050 BCE)
IRON_AGE = 2 # (c.1050 BCE - c.500 BCE)
MIDDLE_AGE = 3 
RENAISSANCE = 4
MACHINE_AGE = 5
ATOMIC_AGE = 6

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

class choronaut: # A choronaut is a chrono ranger who plays cards to explore histories.
    def __init__(self, name):
        self.name = name
        self.occupation = CLASS_CIVILIAN

class history: # 
    def __init__(self, age = STONE_AGE, seed = 0): # A new possible history starts from [age] and randomize with [seed]
        pass    # _TO_BE_CONTINUED_

def main(): # Main loop about what a player can do in this game.
    c = choronaut("John Smith") # Init a new player.
    h = history()   # Legend has ended, while history begins.

if __name__ == "__main__":
    main()
