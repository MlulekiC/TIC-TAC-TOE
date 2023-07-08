import random
"""
We need to create the Player base class
"""

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
