# importing tkinter module
# importing ttk from tkinter

from tkinter import Tk, StringVar
from tkinter.ttk import Label, Entry, Frame, Button 


# creating root window
# creating root title, geometry

root = Tk()
root.title("Calculator")
root.geometry("500x300")
root.resizable(0, 0)
root.configure(background="light pink")


# Label
label = Label(root, text="----CALCULATOR----", font=("verdana", 10, "bold"))
label.grid_location(x=1, y=2)


# creation of a Equation holding variable

equation = StringVar()

expression = ""

equation.set(expression)
# Defining function to get response from button clicked by user


def clicked(num):

    global expression

    expression += str(num)

    equation.set(expression)


def Delete():
    global expression

    expression = expression[:len(expression)-1]

    equation.set(expression)


def equal2():
    global expression

    try:

        equation.set(eval(expression))
        expression = ""

    except:

        equation.set("ERROR")
        expression = ""


def clear():

    global expression

    expression = ""

    equation.set(expression)


# creating output area
show = Entry(root, textvar=equation, width=50, ).pack()


# creating frame

frame = Frame(root)
frame.pack()


# buttons

num1 = Button(frame, text="1", command=lambda: clicked(1)
              ).grid(row=0, column=0)
num2 = Button(frame, text="2", command=lambda: clicked(2)
              ).grid(row=0, column=1)
num3 = Button(frame, text="3", command=lambda: clicked(3)
              ).grid(row=0, column=2)
num4 = Button(frame, text="4", command=lambda: clicked(4)
              ).grid(row=1, column=0)
num5 = Button(frame, text="5", command=lambda: clicked(5)
              ).grid(row=1, column=1)
num6 = Button(frame, text="6", command=lambda: clicked(6)
              ).grid(row=1, column=2)
num7 = Button(frame, text="7", command=lambda: clicked(7)
              ).grid(row=2, column=0)
num8 = Button(frame, text="8", command=lambda: clicked(8)
              ).grid(row=2, column=1)
num9 = Button(frame, text="9", command=lambda: clicked(9)
              ).grid(row=2, column=2)
dot = Button(frame, text=".", command=lambda: clicked(".")
             ).grid(row=3, column=0)
num0 = Button(frame, text="0", command=lambda: clicked(0)
              ).grid(row=3, column=1)
delete = Button(frame, text="DEL", command=Delete).grid(row=3, column=2)

mult = Button(frame, text="x", command=lambda: clicked("x")
              ).grid(row=0, column=3)
div = Button(frame, text="/", command=lambda: clicked("/")
             ).grid(row=1, column=3)
sub = Button(frame, text="-", command=lambda: clicked("-")
             ).grid(row=2, column=3)
plus = Button(frame, text="+", command=lambda: clicked("+")
              ).grid(row=3, column=3)
clear = Button(frame, text="clear", command=clear).grid(row=4, column=1)
equal2 = Button(frame, text="=", command=equal2).grid(row=4, column=2)
#fact=Button(frame, text="!", command=num_5)
#power=Button(frame, text="^", command=num_5)


close = Button(root, text="Quit", width=8, command=root.destroy)
close.pack()


# infinite loop for root window
root.mainloop()
