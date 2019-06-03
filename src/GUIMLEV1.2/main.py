from Mle import *
from UtilBar import *
from NavBar import *
from tools import *
from DisplayWindow import *
import controller as ctrl
from dataTable import *

ctrl.init_utilBar()
ctrl.init_navBar()
ctrl.init_toolBar()

dataTable = IHM(displayWindow,20,75)
dataTable.grid(column=0,row=0)

MLE.mainloop()