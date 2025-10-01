# Create a GUI Calendar using Tkinter
import tkinter as tk
import calendar
root = tk.Tk()
root.title("Calendar")
year = 2026
cal = calendar.TextCalendar().formatyear(year)
text = tk.Text(root)
text.insert(tk.END, cal)
text.pack()
root.mainloop()
