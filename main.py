import numpy as np
from time import sleep
import misc
import bda_lib
import os.path

statOptions = np.array(["Mean temperature","Mean growth rate","Standard deviation of temperature","Standard deviation of growth rate","Mean cold growth rate","Mean hot growth rate"])
statOptionsDict={1:'Mean Temperature',2:'Mean Growth rate',3:'Std Temperature',4:'Std Growth rate',5:'Rows','6':'Mean Cold Growth rate','7':'Mean Hot Growth rate'}
menu = np.array(["Load Data","Filter Data","Display Statistics","Generate Plots","Quit"])
data = []
dataOri = []

while True:
    
    choice = misc.displayMenu(menu)

    if choice == 1:
        print("\nYour datefile should be in the same directory as this script and be of the .csv format")
        fileN=input("Input filename:")
        if os.path.exists(fileN):    
            if fileN.endswith(".csv"):
                dataOri = bda_lib.dataLoad(fileN)
                data = dataOri
            else:
                print("The file is not a .csv\n")
        else:
            print("File does not exist\n")
        
    elif choice == 2:
        if data != []:
            
            print("to be done")
        else:
            print("No data has been loaded\n")
            
    elif choice == 3:
        if data != []:
            opt = misc.displayMenu(statOptions)
            optStat = statOptionsDict[opt]
            print("{:s}: {:d}".format(optStat,bda_lib.dataStatistics(data,optStat)))
        else:
            print("No data has been loaded\n")

    elif choice == 4:
        if data !=[]:
            bda_lib.dataPlot(data)
        else:
            print("No data has been loaded\n")
        
    elif choice == 5:
        print("Quitting... Have a nice day")
        sleep(2)
        break
