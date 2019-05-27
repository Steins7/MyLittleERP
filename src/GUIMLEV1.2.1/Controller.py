import tkinter as tk
from Gui import *

class Controller :

    def __init__(self):
        self.gui = Gui(self)

    def changePage(self,i):
        self.gui.changePage(i)

