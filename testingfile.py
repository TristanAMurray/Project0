import sys

DEBUG = False

def read_number(prompt):
    """Take user input for size of the board."""
    input_size = input(prompt)
    try:
        return int(input_size)
    except:
        print("ERROR: I need a number, nothing else.")
        sys.exit(1)

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
    def __init__(self, columns, rows):
        self.board = [[None for j in range(0, rows)] for i in range(0, columns)]
    def receive_move(self, x, y, who):
        self.board[x - 1][y - 1] = who 
    def display(self):
        i = 1
        columns = len(self.board)
        rows = len(self.board[0])
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
                        if (current_height == 2):
                            # and (i == y) and (j == x):
                            found_move = None
                            for board_column in self.board:
                                debug_now(f"board_column {board_column}")
                                for board_row in board_column:
                                    if board_row is not None:
                                        found_move = board_row 
                            if found_move is not None:
                                write_now(f"  {found_move}  ")
                            else:
                                write_now("     ")
                    if j < columns:
                        write_now("|")
                    j = j + 1
                write_now("\n")
                current_height = current_height + 1
            i = i + 1

sizeinput = read_number("How wide should the board be? ")
sizeinput2 = read_number("How long should the board be? ")

x_move = read_number("What should the x position of your move be? ")
y_move = read_number("What should the y position of your move be? ")
                    
game = ttt_game(sizeinput, sizeinput2)

game.receive_move(x_move, y_move, "*")

game.display()