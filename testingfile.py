import sys

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

def print_ttt_board(size1, size2):
    """Print a tic-tac-toe board with X columns and Y rows."""
    i = 0
   
    while i < size1:
        # The code inside these loops isn't quite correct yet.
        write_now(f"DEBUG: i is {i}\n")
        j = 0
        while j < size2:
            write_now(f"DEBUG: j is {j}\n")
            write_now("---")
            # You'll need to choose where to include newlines now.
            write_now("|")
            write_now("---")
            write_now("|")
            write_now("---")
            j = j + 1
        i = i + 1
      

print_ttt_board(sizeinput,sizeinput2)
