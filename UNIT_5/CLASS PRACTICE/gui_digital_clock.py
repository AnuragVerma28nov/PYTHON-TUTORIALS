# Create a GUI digital clock using Tkinter
import tkinter as tk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=("Arial", 50), bg="black", fg="white")
label.pack()
def update_time():
    label.config(text=strftime("%H:%M:%S"))
    label.after(1000, update_time)
update_time()
root.mainloop()
