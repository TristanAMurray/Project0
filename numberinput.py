import sys

def get_integer_input(prompt):
    """Return an integer from the user, prompting with PROMPT (a string).
    If the user enters something other than an integer, throw an
    exception."""
    input_str = input(prompt)
    try:
        num = int(input_str)
    except:
        print("ERROR: I need a number, nothing else.")
    return num

num1 = get_integer_input("What is your number? ")
num2 = get_integer_input("What is your second number? ")

if num1 > num2:
    tmp = num1
    num1 = num2
    num2 = tmp

sum = 0
i = num1

while i <= num2:
    sum = sum + i 
    i = i + 1

print("Sum of {0} through {1} is {2}" .format(num1, num2, sum))

### This block was just for experimenting with if/else statements.
### It doesn't serve any purpose in the program, so I've commented
### it out for now.  You can remove it when you're ready.  -Karl
#
# if True:
#     print("This is what happens in the 'true' case.")
#     if 3 == int("3"):
#         print("Yep, int() behaves as expected.")
#     elif 3 == int("4"):
#         print("This line should never be printed.")
#     elif 3 == int("3"):
#         print("Interestingly, this line shouldn't be printed either.  Why not?")
#     else:
#         print("This line will never be printed either!  Sheesh.")
# else:
#     print("This would be what happens in the 'false' (non-true) case.")
