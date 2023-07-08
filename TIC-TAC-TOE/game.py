import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we'll use a single list to represent our board
        self.current_winner = None # This keeps track wether there's a current winnner and who it is

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums(): # It's static coz it doesn't belong to any specific board
        # -> We're just gonna print out which numbers corresponds to which spot
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    # returns an empty list
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    """ moves = [] # initialise moves
        for (i, spot) in enumerate(self.board):
             
            #enumerate is gonna create a list, and assign tuples that have the index 
            #comma the value in that index e.g: ["x", "x", "o"] -> [(0, "x"), (1, "x"), (2, "o")]
            
            if spot == " ":
                moves.append(i) # Append the index of that spot to moves
        return moves
    """

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ") # counts the number of blanks in our board and returns it

    def make_move(self, square, letter):
        # if valid move, then make the move(assign square to letter, then return true. else return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere... we have to check all combinations
        # first let's check the row
        row_index = square // 3
        row = self.board[row_index*3 : (row_index +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        column_index = square % 3
        column = [self.board[column_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check Diagonals
        """
        but only the square is an even number (0, 2, 4, 5, 6, 8)
        these are the only moves possible to win a diagonal
        """
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to Bottom left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all these checks fail
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X" # starting letter
    # iterate while the game still has empty squares( we don't have to worry about the winner because we'll just return that which breaks the loop
    while game.empty_squares():
        # Get the move  from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Let's define a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board() # this shows us the updated board where the spot has been taken
                print("") # empty line

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins")
                return letter

            # after we made our move, we need to alternate letters
            letter = "O" if letter == "X" else "X" # this is equivalent to the next 4 lines
            """ 
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
            """
        # tiny pause for the computer to respond
        time.sleep(1.2)
    if print_game:
        print("It's a Tie")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe() # Our game instance
    play(t, x_player,o_player, print_game=True)
