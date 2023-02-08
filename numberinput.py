import tkinter

prompt_1 = "What is your number?"
prompt_2 = "What is your second number?"

t = tkinter.Tk()

frame = tkinter.Frame(t, borderwidth=5)
frame.pack(fill=tkinter.BOTH, expand=1)
label = tkinter.Label(frame, text="Button Example")
label.pack(fill=tkinter.X, expand=1)

button = tkinter.Button(frame, text="Exit", command=t.destroy)
button.pack(side=tkinter.BOTTOM)
t.mainloop()
