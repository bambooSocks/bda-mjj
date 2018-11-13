import numpy as np
from time import sleep
import misc
import bda
import os.path

# Global variables
statOptions = np.array(["Mean temperature","Mean growth rate","Standard deviation of temperature","Standard deviation of growth rate","Rows","Mean cold growth rate","Mean hot growth rate"])
statOptionsDict={1:'Mean Temperature',2:'Mean Growth rate',3:'Std Temperature',4:'Std Growth rate',5:'Rows',6:'Mean Cold Growth rate',7:'Mean Hot Growth rate'}
menu = np.array(["Load Data","Filter Data","Display Statistics","Generate Plots","Quit"])
current_data = np.array([])
orig_data = []
activeFilt = np.zeros(6)


# Main Loop
while True:
    
    misc.printFilter(activeFilt)
    
    choice = misc.displayMenu(menu)
    
    # Calls the dataLoad function
    if choice == 1:
        print("\nYour datafile should be in the same directory as this script")
        filename=input("Input file name: ")
        # Checks if the file exists
        if os.path.exists(filename):    
            orig_data = bda.dataLoad(filename)
            current_data = orig_data
        else:
            print("File does not exist\n")
        
    # Applies filters
    elif choice == 2:
        while True:
            misc.printFilter(activeFilt)
            filt = misc.displayMenu(np.array(["Apply Bacteria Filter","Apply Upper Growth Rate Filter","Apply Lower Growth Rate Filter","Clear Filters","Quit Filter Menu"]))
            # Bacteria filters
            if filt == 1 and np.size(current_data) != 0:
                print("Exclude bacteria type:")
                filtCho = misc.displayMenu(np.array(["Salmonella enterica","Bascillus cereus","Listeria","Brochothtrix thermosphacta"]))
                current_data = current_data[current_data[:,2]!=filtCho]
                activeFilt[filtCho-1] +=1
            # Upper growth rate bound filter
            elif filt == 2 and np.size(current_data) != 0:
                filtCho = float(input("Input upper bound: "))
                current_data = current_data[current_data[:,1]<=filtCho]
                activeFilt[4] += filtCho
            # Lower growth rate bound filter
            elif filt == 3 and np.size(current_data) != 0:
                filtCho = float(input("Input lower bound: "))
                current_data = current_data[current_data[:,1]>=filtCho]
                activeFilt[5] += filtCho
            # Clears all filters
            elif filt == 4:
                print("All filters has been removed")
                current_data = orig_data
                activeFilt = np.zeros(6)
            # Terminates the filter menu
            elif filt == 5:
                break
            # Not data in the current buffer
            elif np.size(current_data) == 0:
            	print("No data, clear the filters or load new data before you continue")
            
    # Calls the data statistics funtion
    elif choice == 3:
        if np.size(current_data) != 0:
            # Displays menu with options for statistics
            opt = misc.displayMenu(statOptions)
            optStat = statOptionsDict[opt]
            print("{}: {}".format(optStat,bda.dataStatistics(current_data,optStat)))
        else:
            print("No data has been loaded\n")
        
    # Plots data
    elif choice == 4:
        if np.size(current_data) != 0:
            bda.dataPlot(current_data)
        else:
            print("No data has been loaded\n")
            
    # Terminates the program  
    elif choice == 5:
        print("Terminating... Have a nice day!")
        sleep(2)
        break
