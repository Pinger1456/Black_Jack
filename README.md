# Blackjack Game

## Overview
This is a Python implementation of the classic card game **Blackjack**, also known as **21**. The goal of the game is to get a hand as close as possible to 21 without going over. The game allows the player to bet money, hit, stand, or double down. The dealer follows standard Blackjack rules, hitting until they reach at least 17 points.

This project is a great example of a simple, text-based game using Python's basic features like control structures, randomization, and I/O operations. The game does not include splitting or insurance rules.

## Rules
- Try to get as close to 21 without going over.
- Kings, Queens, and Jacks are worth 10 points.
- Aces are worth 1 or 11 points.
- Cards 2 through 10 are worth their face value.
- You can choose to **(H)**it to take another card or **(S)**tand to stop.
- You can **(D)**ouble down to increase your bet but must hit exactly one more time before standing.
- In case of a tie, the bet is returned to the player.
- The dealer stops hitting at 17.

## How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blackjack-game.git
   cd blackjack-game
2. Install dependencies (if any): This project does not have external dependencies, but make sure you have Python installed.
3. Run the game:
   ```bash
   python blackjack.py
4. Follow the on-screen instructions to place bets, hit, stand, or double down.
Project Structure
blackjack.py: The main script that runs the Blackjack game.
config.py: A configuration file that defines suits and other game constants.
Features
Randomized card deck: The deck is shuffled before each game, providing a fair deal to both player and dealer.
Betting system: Players start with $5000 and can bet each round. The game ends when the player runs out of money.
Basic AI for the dealer: The dealer automatically plays according to the game's rules, hitting until they reach 17 or higher.
Doubling down: Players can double their bet in exchange for committing to exactly one more card.
Requirements
Python 3.x
Future Enhancements
Implement card splitting.
Add insurance and surrender options.
Create a graphical user interface (GUI) for a better user experience.
Add multiplayer support.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Game logic inspired by the classic Blackjack card game.
Original code from Al Sweigart's Big Book of Small Python Projects.
