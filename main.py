"""
This module implements a simple blackjack game.
It imports the blackjack module and runs the game if executed as a standalone script.
"""

from blackjack import blackjack

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    blackjack.run_game()
# print(blackjack.getDeck())
