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

sizeinput = read_number("How wide should the board be? ")
sizeinput2 = read_number("How long should the board be? ")

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
    i = 1
   
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
                    write_now("     ")
                if j < columns:
                    write_now("|")
                j = j + 1
            write_now("\n")
            current_height = current_height + 1
        i = i + 1
      

print_ttt_board(sizeinput,sizeinput2)

x_move = read_number("What should the x position of your move be? ")
y_move = read_number("What should the y position of your move be? ")

print(f"x_move is {x_move}")
print(f"y_move is {y_move}")