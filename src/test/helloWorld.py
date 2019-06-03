import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

root = tk.Tk()
lab = tk.Label(root, text="Hello World",justify="left")
root.wm_title("Graphe Matplotlib dans Tkinter")
root.columnconfigure(1,weight=2)
root.columnconfigure(2,weight=7)
root.rowconfigure(2,weight=2)
lab.grid(row=3, column=1,sticky="n")


fram = tk.Frame(root)
fram.rowconfigure(2,weight=2)
fram.grid(row=2, column=1,columnspan=2,sticky="nsew")

button1 = tk.Button(fram, text="Btn1",fg="red",command=lambda:controller.show_frame(StartPage))
button2 = tk.Button(fram, text="Btn2",fg="green")
button3 = tk.Button(fram, text="Btn3",fg="blue")
button4 = tk.Button(fram, text="Btn4",fg="purple")

button1.grid(row=2, column=1,sticky="nsew")
button2.grid(row=2, column=2,sticky="nsew")
button3.grid(row=2, column=3,sticky="nsew")
button4.grid(row=2, column=4,sticky="nsew")

root.wm_title("Graphe Matplotlib dans Tkinter")
 
fig = Figure(figsize=(6, 4), dpi=150)
ax = fig.add_subplot(211)
ax.plot(range(100), [5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3,5, 4, 2, 6, 9, 8, 7, 1, 2, 3])
ax.plot(range(100), [7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3,7, 4, 6, 6, 9, 3, 7, 7, 2, 3])

ay = fig.add_subplot(212)
ay.plot(range(10), [7, 4, 6, 6, 9, 3, 7, 7, 2, 3])

graph = FigureCanvasTkAgg(fig, master=root)
canvas = graph.get_tk_widget()
canvas.grid(row=3, column=2)

#toolbar = NavigationToolbar2TkAgg(graph,root)

class StartPage(tk.Frame) :
    def __init__(self,parent,controller) :
        tk.Frame.__init__(self,parent)  
        label = tk.Label(self,text="StartPage",font=LARGE_FONT)
        label.grid(row=5,column=5)
        button1SP = tk.Button(self,text="page two",command=lambda:controller.show_frame(PageTwo))
        button1SP.grid(row=3,column=4)

class PageTwo(tk.Frame) :
    def __init__(self,parent,controller) :
        tk.Frame.__init__(self,parent)  
        label = tk.Label(self,text="PageTwo",font=LARGE_FONT)
        label.grid(row=5,column=5)
        button1P2 = tk.Button(self,text="back home",command=lambda:controller.show_frame(StartPage))
        button1P2.grid(row=3,column=3)


root.mainloop()
