from Mle import *
from UtilBar import *
from NavBar import *
from tools import *
from DisplayWindow import *

strFile = "file"
strEdit = "edit"
strSelect = "selection"
strHelp = "help"
strQuit = "quit"


def B2():
    b2=tk.Button(utilBar,text="it works !",fg="black",bg="white",command=lambda:B1())
    b2.grid(column=1,row=0,sticky="nsew")

def B1():
    b1=tk.Button(utilBar,text="change",fg="black",bg="white",command=lambda:B2())
    b1.grid(column=0,row=0,sticky="nsew")

def init_utilBar():

    btnFile = tk.Button(utilBar,text=strFile,fg="black",bg="white",name=strFile,command=lambda:menu(strFile))
    btnFile.grid(column=0,row=0,sticky="nsew")
    btnEdit = tk.Button(utilBar,text=strEdit,fg="black",bg="white",name=strEdit,command=lambda:menu(strEdit))
    btnEdit.grid(column=1,row=0,sticky="nsew")
    btnSelect = tk.Button(utilBar,text=strSelect,fg="black",bg="white",name=strSelect,command=lambda:menu(strSelect))
    btnSelect.grid(column=2,row=0,sticky="nsew")
    btnHelp = tk.Button(utilBar,text=strHelp,fg="black",bg="white",name=strHelp,command=lambda:menu(strHelp))
    btnHelp.grid(column=3,row=0,sticky="nsew")
    btnQuit = tk.Button(utilBar,text=strQuit,fg="black",bg="white",name=strQuit,command=lambda:MLE.quit())
    btnQuit.grid(column=4 ,row=0,sticky="nsew")


def init_navBar():
    btnShowFlow = tk.Button(navBarFlow,text="+",fg="black",bg="white",name="showFlow",command=lambda:showFlow())
    btnShowFlow.grid(column=0,row=0,sticky="nsew")
    btnShowAccount = tk.Button(navBarAccount,text="+",fg="black",bg="white",name="showAccount",command=lambda:showAccount())
    btnShowAccount.grid(column=0,row=0,sticky="nsew")
    btnShowInventory = tk.Button(navBarInventory,text="+",fg="black",bg="white",name="showInventory",command=lambda:showInventory())
    btnShowInventory.grid(column=0,row=0,sticky="nsew")

def init_toolBar():
    btnCreateFlow = tk.Button(toolBar,text="Create Flow",fg="black",bg="white",name="createFlow",command=lambda:CreateFlow())
    btnCreateFlow.grid(column=0,row=1,sticky="nsew")