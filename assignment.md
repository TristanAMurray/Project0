* 2023-10-18

  - Get Git commit working.
  - Make player errors be non-fatal.
  - Put newlines at ends of errors and other messages.
  - Do something appropriate if board is full.
  - Detect a win.

* 2023-07-12

  Make sure players use different symbols.
  Add a way to alternate turns between players.

* 2023-06-25

  Add error checking.

* 2023-06-05

  Take any single character as the move from the user, and record it
  in the board so that when the board is printed, we see that
  character (which might or might not be "*" -- it depends on what the
  user gave).

* 2023-05-22

  Unify ttt_game.display() and print_ttt_board().

  Maybe start alternating players.

  Don't forget doc strings too.

* 2023-05-18

  Got printing a single move in the middle of a cell working.
  
  Set up a data structure to keep track of the game.


* 2023-04-23

  We've got board-printing working, and move-prompting working.

  For next time, we want to print the moves that are on the board,
  which means having some kind of game-state data structure.

* 2023-03-23
  
  Make the code display an actual tic-tac-toe board even when DEBUG is set to false.
  Same as assignment for 3/5/2023, because Florida happened :-).

* 2023-03-5 

  Increase cell size to allow for displaying of user input and take user input for board size.

* 2023-02-23

  Draw a tic-tac-toe board on the screen, using normal characters (such
  as "-", "_", ".", "|", and other things found on a normal keyboard).

* 2023-01-29

  Read a number from the user and print "this is the number x" and then print the sum of all the numbers from the lower to the higher. 

  BONUS: Learn to handle integer conversion exceptions.

  Research how to define a function and call a function