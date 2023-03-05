import sys

def print_ttt_board(x, y):
    """Print a tic-tac-toe board with X columns and Y rows."""
    i = 0
    j = 0
    while i < x:
        while j < y:
            # The code from this point on isn't quite correct.
            print ("   |")  
            print ("----")
            j = j + 1
        i = i + 1

print_ttt_board(3, 3)
