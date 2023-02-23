
prompt_1 = "What is your number?"
fnumber = input(prompt_1)
num1 = int(fnumber)

prompt_2 = "What is your second number?"
fnumber2 = input(prompt_2)
num2 = int(fnumber2)

sum = range(num1, num2)
print("Sum of {0} through {1} is {2}" .format(num1, num2, sum))

if True:
    print("This is what happens in the 'true' case.")
    if 3 == int("3"):
        print("Yep, int() behaves as expected.")
    elif 3 == int("4"):
        print("This line should never be printed.")
    elif 3 == int("3"):
        print("Interestingly, this line shouldn't be printed either.  Why not?")
    else:
        print("This line will never be printed either!  Sheesh.")
else:
    print("This would be what happens in the 'false' (non-true) case.")
