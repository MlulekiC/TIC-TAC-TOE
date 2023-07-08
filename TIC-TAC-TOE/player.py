import math
import random


class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter

    # Creating the function that allows all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # We want this function to iterate until the user chooses a valid spot
        valid_square = False
        value = None # Since the user hasn't input a value yet
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move(0-9): ")
            """
            We're gonna check that this is a correct value by trying to cast
            it to an integer, and if it's not we say it's invalid, if that spot
            is not available on the board, we also sa it's invalid
            """
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, Try again")
        return value # this is the human player's next move
















