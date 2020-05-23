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

class card: # Cards are heroes, events, locations, treasures, etc. Cards have color used for match-3.
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.color = COLOR_RED

def main(): # Main loop about what a player can do in this game.
    pass

if __name__ == "__main__":
    main()
