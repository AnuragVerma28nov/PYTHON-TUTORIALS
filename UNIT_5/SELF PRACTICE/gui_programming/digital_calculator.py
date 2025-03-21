# Digital Calculator
# Description: Create a calculator using Tkinter

from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("240x340")
root.configure(bg="#333333")
root.resizable(0, 0)

# Entry widget for displaying the input and output
entry = Entry(root, font=("Times New Roman", 18), bd=5, insertwidth=2, width=14, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Global expression variable to store the calculation
expression = ""

# Define functions for the buttons
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, END)
    entry.insert(END, expression)

def press_equal():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression
        entry.delete(0, END)
        entry.insert(0, result)
        expression = result  # Update expression with the result
    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Error")
        expression = ""

def press_clear():
    global expression
    expression = ""
    entry.delete(0, END)

# Creating buttons
button_0 = Button(root, text="0", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(0), height=2, width=6)
button_1 = Button(root, text="1", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(1), height=2, width=6)
button_2 = Button(root, text="2", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(2), height=2, width=6)
button_3 = Button(root, text="3", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(3), height=2, width=6)
button_4 = Button(root, text="4", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(4), height=2, width=6)
button_5 = Button(root, text="5", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(5), height=2, width=6)
button_6 = Button(root, text="6", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(6), height=2, width=6)
button_7 = Button(root, text="7", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(7), height=2, width=6)
button_8 = Button(root, text="8", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(8), height=2, width=6)
button_9 = Button(root, text="9", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press(9), height=2, width=6)

button_plus = Button(root, text="+", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press("+"), height=2, width=6)
button_minus = Button(root, text="-", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press("-"), height=2, width=6)
button_multiply = Button(root, text="*", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press("*"), height=2, width=6)
button_divide = Button(root, text="/", bg="#A73278", fg="white", font=("Times New Roman", 12), command=lambda: press("/"), height=2, width=6)

button_equal = Button(root, text="=", bg="#A73278", fg="white", font=("Times New Roman", 12), command=press_equal, height=2, width=6)
button_clear = Button(root, text="Clear", bg="#A73278", fg="white", font=("Times New Roman", 12), command=press_clear, height=2, width=6)

# Placing widgets on the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

root.mainloop()
