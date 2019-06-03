import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# code trouve sur internet. https://python.developpez.com/actu/127261/Creer-un-tableau-interactif-en-python-avec-Tkinter/

class IHM(tk.Frame): 
    def __init__(self, fenetre, height, width): 
        tk.Frame.__init__(self, fenetre) 
        self.numberLines = height 
        self.numberColumns = width 
        self.grid(sticky="nsew") 
        self.data = list() 
        for i in range(self.numberLines): 
            line = list() 
            for j in range(self.numberColumns): 
                cell = tk.Entry(self, width=1) 
                cell.insert(0, 0) 
                line.append(cell) 
                cell.grid(row = i, column = j) 
            self.data.append(line) 
  
        self.results = list() 
        for i in range(self.numberColumns): 
            cell = tk.Entry(self,width=1) 
            cell.insert(0, 0) 
            cell.grid(row = self.numberLines, column = i) 
            self.results.append(cell) 
        self.buttonSum =  tk.Button(self, text="somme des colonnes", fg="red",width=2, command=self.sumCol) 
        self.buttonSum.grid(row = self.numberLines, column = self.numberColumns) 
  
    def sumCol(self): 
        for j in range(self.numberColumns): 
            result = int(0) 
            for i in range(self.numberLines): 
                result += int(self.data[i][j].get()) 
            self.results[j].delete(0, END) 
            self.results[j].insert(0, result)