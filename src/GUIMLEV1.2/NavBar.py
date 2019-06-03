from Mle import *


navigationBar = tk.Label(MLE)
navigationBar.columnconfigure(0,weight=0)
navigationBar.columnconfigure(1,weight=1)
navigationBar.rowconfigure(0,weight=1)
navigationBar.rowconfigure(1,weight=1)
navigationBar.rowconfigure(2,weight=1)
navigationBar.rowconfigure(3,weight=1)
navigationBar.rowconfigure(4,weight=1)
navigationBar.rowconfigure(5,weight=1)
navigationBar.rowconfigure(6,weight=1)
navigationBar.rowconfigure(7,weight=1)
navigationBar.rowconfigure(8,weight=1)
navigationBar.rowconfigure(9,weight=1)

navigationBar.grid(row=1,column=0,sticky="nsew")
navBarTitle = tk.Label(navigationBar,text="Navigation Bar")
navBarTitle.grid(row=0,column=0,sticky="w")

navBarFlow = tk.Label(navigationBar)
navBarFlow.grid(row=1,column=0,sticky="nsew")
navBarFlow.columnconfigure(0,weight=0)
navBarFlow.columnconfigure(1,weight=1)
navBarFlowTitle = tk.Label(navBarFlow,text = "money flow")
navBarFlowTitle.grid(row=0,column=1,sticky="nw")


navBarAccount = tk.Label(navigationBar)
navBarAccount.grid(row=2,column=0,sticky="nsew")
navBarAccount.columnconfigure(0,weight=0)
navBarAccount.columnconfigure(1,weight=1)
navBarAccountTitle = tk.Label(navBarAccount,text = "account")
navBarAccountTitle.grid(row=0,column=1,sticky="nw")


navBarInventory = tk.Label(navigationBar)
navBarInventory.grid(row=3,column=0,sticky="nsew")
navBarInventory.columnconfigure(0,weight=0)
navBarInventory.columnconfigure(1,weight=1)
navBarInventoryTitle = tk.Label(navBarInventory,text = "inventory")
navBarInventoryTitle.grid(row=0,column=1,sticky="nw")