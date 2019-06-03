import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
app = tk.Tk()
app.wm_title("Graphe Matplotlib dans Tkinter")
 
fig = Figure(figsize=(6, 4), dpi=96)
ax = fig.add_subplot(121)
ax.plot(range(10), [5, 4, 2, 6, 9, 8, 7, 1, 2, 3])
ax.plot(range(10), [7, 4, 6, 6, 9, 3, 7, 7, 2, 3])

ay = fig.add_subplot(122)
ay.plot(range(10), [7, 4, 6, 6, 9, 3, 7, 7, 2, 3])

graph = FigureCanvasTkAgg(fig, master=app)
canvas = graph.get_tk_widget()
canvas.grid(row=1, column=1)
 
app.mainloop()