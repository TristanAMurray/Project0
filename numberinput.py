import time
import tkinter
import tkinter.simpledialog
import tkinter.messagebox

prompt_1 = "What is your number?"
prompt_2 = "What is your second number?"

num_1 = int(tkinter.simpledialog.askinteger("First integer", prompt_1))
num_2 = int(tkinter.simpledialog.askinteger("Second integer", prompt_2))

total = 0
for i in range(num_1, num_2 + 1):
    total += i
    tkinter.messagebox.showinfo("Current Total", f"Adding {i}, to get a new total of {total}")

# t = tkinter.Tk()
# 
# frame = tkinter.Frame(t, borderwidth=5)
# frame.pack(fill=tkinter.BOTH, expand=1)
# 
# label = tkinter.Label(frame, text="Button Example")
# label.pack(fill=tkinter.X, expand=1)
# 
# button = tkinter.Button(frame, text="Exit", command=t.destroy)
# button.pack(side=tkinter.BOTTOM)

# t.mainloop()

### References: ###
#
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/3/library/tkinter.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
