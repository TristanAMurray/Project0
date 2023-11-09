import sys

DEBUG = True

def read_number(prompt):
    """Take user input for size of the board."""
    while True:
        input_size = input(prompt)
        try:
            return int(input_size)
        except Exception as e:
            print("ERROR: I need a number, nothing else.\n")
            print(f"ERROR: Exception received: {e}\n")

def read_symbol(prompt):
    """Take user input for the symbol that represents their moves."""
    while True:
        input_symbol = input(prompt)
        if len(input_symbol) == 1:
            return input_symbol
        else:
            print("ERROR: Only one character is allowed.\n")

def write_now(msg):
    """Write MSG to stdout, and flush immediately."""
    sys.stdout.write(msg)
    sys.stdout.flush()

def debug_now(msg):
    """Iff global DEBUG flag is not False, write MSG to stdout
    with "DEBUG: " prefix, and flush immediately."""
    if DEBUG:
        sys.stdout.write("DEBUG: ")
        write_now(msg)

class ttt_game:
    def __init__(self, size):
        self.board = [[None for j in range(0, size)] for i in range(0, size)]
    def receive_move(self, x, y, who):
        """Receive one move X,Y from Player WHO."""
        out_of_bounds_errors = []
        if x > len(self.board):
            out_of_bounds_errors.append(
                f"ERROR: Move {x} is wider than board width {len(self.board)}.")
        if y > len(self.board[0]):
            out_of_bounds_errors.append(
                f"ERROR: Move {y} exceeds board height {len(self.board[0])}.")
        if len(out_of_bounds_errors) != 0:
            for elt in out_of_bounds_errors:
                write_now(elt + "\n")
            return False
        if self.board[x - 1][y - 1] is None:
            self.board[x - 1][y - 1] = who 
        else:
            write_now(f"ERROR: Move \"{self.board[x - 1][y - 1]}\" is already at {x}, {y}.\n")
            return False
        any_open_space = False
        current_x = 0
        while (current_x < len(self.board)) and (any_open_space == False):
            current_y = 0
            while (current_y < len(self.board[current_x])) and (any_open_space == False):
                if self.board[current_x][current_y] is None:
                    any_open_space = True
                current_y = current_y + 1
            current_x = current_x + 1
        if any_open_space == False:
            write_now("No empty spots left on board.\n")
        return True

    def display(self):
        i = 1
        columns = len(self.board)
        rows = len(self.board[0])
        write_now("\n")
        while i <= rows:
            desired_height = 3
            current_height = 1
            while current_height <= desired_height:
                j = 1
                while j <= columns:
                    if current_height == desired_height:
                        if i < rows:
                            write_now("_____")
                        else:
                            write_now("     ")
                    else:
                        if (current_height == 2) and self.board[j - 1][i - 1] is not None:
                            write_now(f"  {self.board[j - 1][i - 1]}  ")
                        else:
                            write_now("     ")
                    if j < columns:
                        write_now("|")
                    j = j + 1
                write_now("\n")
                current_height = current_height + 1
            i = i + 1
        write_now("\n")

sizeinput = read_number("How big should the board be? ")

player1_symbol = read_symbol("What symbol does Player 1 want to represent their moves? ")
player2_symbol = read_symbol("What symbol does Player 2 want to represent their moves? ")

game = ttt_game(sizeinput)

whose_turn = 1

while True:
    x = read_number(f"What should the x position of Player {whose_turn}'s move be? ")
    y = read_number(f"What should the y position of Player {whose_turn}'s move be? ")
    if whose_turn == 1:
        successful_move = game.receive_move(x, y, player1_symbol) 
        if successful_move == True:
            whose_turn = 2    
    elif whose_turn == 2:         
        successful_move = game.receive_move(x, y, player2_symbol)
        if successful_move == True:
            whose_turn = 1
    game.display()