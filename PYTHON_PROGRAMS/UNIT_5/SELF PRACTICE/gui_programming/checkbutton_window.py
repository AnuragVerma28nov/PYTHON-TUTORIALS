# checkbutton window

import tkinter as tk

root = tk.Tk()
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=checkbox_var)
checkbox.pack()

root.mainloop()