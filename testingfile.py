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
            sys.stdout.write(f"DEBUG: j is {j}\n")
            sys.stdout.flush()
            sys.stdout.write("__")
            # You'll need to choose where to include newlines now.
            sys.stdout.flush()
            sys.stdout.write("|")
            sys.stdout.flush()
            sys.stdout.write("__")
            sys.stdout.flush()
            sys.stdout.write("|")
            sys.stdout.flush()
            sys.stdout.write("__")
            j = j + 1
        i = i + 1

print_ttt_board(3, 3)
