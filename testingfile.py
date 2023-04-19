import sys

DEBUG = False

def board_size_input(prompt):
    """Take user input for size of the board."""
    input_size = input(prompt)
    try:
        return int(input_size)
    except:
        print("ERROR: I need a number, nothing else.")
        sys.exit(1)

sizeinput = board_size_input("How wide should the board be?")
sizeinput2 = board_size_input("How long should the board be?")

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

def print_ttt_board(columns, rows):
    """Print a tic-tac-toe board with X columns and Y rows."""
    i = 0
   
    while i < rows:
        debug_now(f"i is {i}\n")
        j = 0
        while j < columns:
            debug_now(f"j is {j}\n")
            write_now("     ")
            write_now("|")
            j = j + 1
        write_now("\n")    
        i = i + 1
      

print_ttt_board(sizeinput,sizeinput2)
