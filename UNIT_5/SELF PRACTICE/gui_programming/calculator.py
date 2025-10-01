# calculator

import tkinter as tk

def add():
    result.set(float(entryl.get()) + float(entry2.get()))

def subtract():
    result.set(float(entryl.get()) - float(entry2.get()))

def multiply(): 
    result.set(float(entryl.get()) * float(entry2.get()))
    
def divide():
    result.set(float(entryl.get()) / float(entry2.get()))

root = tk.Tk()
root.title("Simple Calculator")

entryl=tk.Entry(root)
entryl.pack()

entry2=tk.Entry(root)
entry2.pack()

result = tk. DoubleVar() 
result_label= tk.Label(root,textvariable=result)
result_label.pack()

add_button = tk.Button(root, text="Add", command=add) 
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract) 
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply) 
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

root.mainloop()
