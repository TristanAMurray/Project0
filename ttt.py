import sys

DEBUG = True

def read_number(prompt):
    """Take user input for size of the board."""
    input_size = input(prompt)
    try:
        return int(input_size)
    except:
        print("ERROR: I need a number, nothing else.")
        sys.exit(1)

def read_symbol(prompt):
    """Take user input for the symbol that represents their moves."""
    input_symbol = input(prompt)
    if len(input_symbol) == 1:
        return input_symbol
    else:
        print("ERROR: Only one character is allowed.")
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
        """Recieve one move X,Y from Player WHO."""
        if self.board[x - 1][y - 1] is None:
            self.board[x - 1][y - 1] = who 
        else:
            print(f"ERROR: Move \"{self.board[x - 1][y - 1]}\" is already at {x}, {y}.")
            sys.exit(1)
            
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

sizeinput = read_number("How wide should the board be? ")
sizeinput2 = read_number("How long should the board be? ")

player1_symbol = read_symbol("What symbol does Player 1 want to represent their moves? ")
player2_symbol = read_symbol("What symbol does Player 2 want to represent their moves? ")

game = ttt_game(sizeinput, sizeinput2)

p1_x = read_number("What should the x position of Player 1's move be? ")
p1_y = read_number("What should the y position of Player 1's move be? ")

game.receive_move(p1_x, p1_y, player1_symbol)

game.display()

p2_x = read_number("What should the x position of Player 2's move be? ")
p2_y = read_number("What should the y position of Player 2's move be? ")
                    
game.receive_move(p2_x, p2_y, player2_symbol)

game.display()