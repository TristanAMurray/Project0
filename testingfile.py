import sys

def write_now(msg):
    """Write MSG to stdout, and flush immediately."""
    sys.stdout.write(msg)
    sys.stdout.flush()

def print_ttt_board(x, y):
    """Print a tic-tac-toe board with X columns and Y rows."""
    i = 0
    j = 0
    while i < x:
        # The code inside these loops isn't quite correct yet.
        write_now(f"DEBUG: i is {i}\n")
        while j < y:
            write_now(f"DEBUG: j is {j}\n")
            write_now("__")
            # You'll need to choose where to include newlines now.
            write_now("|")
            write_now("__")
            write_now("|")
            write_now("__")
            j = j + 1
        i = i + 1

print_ttt_board(3, 3)
