# namegreet window gui

import tkinter as tk

def update_label():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Simple GUI Example")
root.geometry("300x200")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=update_label)
button.pack(pady=10)

root.mainloop()


