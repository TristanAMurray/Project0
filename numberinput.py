
prompt_1 = "What is your number?"
fnumber = input(prompt_1)
num1 = fnumber

prompt_2 = "What is your second number?"
fnumber2 = input(prompt_2)
num2 = fnumber2

sum = num1 + num2
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))

together_string = prompt_1 + "  <yay>     " + prompt_2
print(f"{together_string}")
