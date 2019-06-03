import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

root = tk.Tk()
fig = fig = Figure(figsize=(6, 4), dpi=150)
figCanvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2TkAgg(figCanvas,root)
root.mainloop()