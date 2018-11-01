import numpy as np
from time import sleep
import misc
import bda_lib

statOptions = np.array(["Mean temperature","Mean growth rate","Standard deviation of temperature","Standard deviation of growth rate","Mean cold growth rate","Mean hot growth rate"])
statOptionsDict={1:'Mean Temperature',2:'Mean Growth rate',3:'Std Temperature',4:'Std Growth rate',5:'Rows','6':'Mean Cold Growth rate','7':'Mean Hot Growth rate'}
menu = np.array(["Load Data","Filter Data","Display Statistics","Generate Plots","Quit"])

while True:

    choice = misc.displayMenu(menu)

    if choice == 1:
        print("Your datefile should be in the same directory as this script")
        data = bda_lib.dataLoad(input("Input filename:"))

    elif choice == 2:
        print("to be done")

    elif choice == 3:
        opt = misc.displayMenu(statOptions)
        optStat = statOptionsDict[opt]
        print("{:s}: {:d}".format(optStat,bda_lib.dataStatistic(data,optStat)))

    elif choice == 4:
        dba_lib.dataPlot(data)

    elif choice == 5:
        print("Quitting... Have a nice day")
        sleep(3)
        break
