import numpy as np
from time import sleep
import misc
import bda_lib
import os.path

# Sets up necesarry values and dictionary
statOptions = np.array(["Mean temperature","Mean growth rate","Standard deviation of temperature","Standard deviation of growth rate","Rows","Mean cold growth rate","Mean hot growth rate"])
statOptionsDict={1:'Mean Temperature',2:'Mean Growth rate',3:'Std Temperature',4:'Std Growth rate',5:'Rows',6:'Mean Cold Growth rate',7:'Mean Hot Growth rate'}
menu = np.array(["Load Data","Filter Data","Display Statistics","Generate Plots","Quit"])
data = []
dataOri = []
activeFilt = np.zeros(6)


# Main Loop
while True:
    
    misc.printFilter(activeFilt)
    
    choice = misc.displayMenu(menu)
    
    #Calls the dataload function
    if choice == 1:
        print("\nYour datafile should be in the same directory as this script")
        fileN=input("Input filename: ")
        #Checks if the file exists
        if os.path.exists(fileN):    
            dataOri = bda_lib.dataLoad(fileN)
            data = dataOri
        else:
            print("File does not exist\n")
        
    #Applies filters
    elif choice == 2:
        if data != []:
            while True:
                misc.printFilter(activeFilt)
                filt = misc.displayMenu(np.array(["Apply Bacteria Filter","Apply Upper Growth Rate Filter","Apply Lower Growth Rate Filter","Clear Filters","Quit Filter Menu"]))
                #Bacteria Filters
                if filt == 1:
                    print("Exclude bacteria type:")
                    filtCho = misc.displayMenu(np.array(["Salmonella enterica","Bascillus cereus","Listeria","Brochothtrix thermosphacta"]))
                    data = data[data[:,2]!=filtCho]
                    activeFilt[filtCho-1] +=1
                #Upper growth rate bound filter
                elif filt == 2:
                    filtCho = float(input("Input upper bound:"))
                    data = data[data[:,1]<=filtCho]
                    activeFilt[4] += filtCho
                #Lower growth rate bound filter
                elif filt == 3:
                    filtCho = float(input("Input lower bound:"))
                    data = data[data[:,1]>=filtCho]
                    activeFilt[5] += filtCho
                #Clears all filters
                elif filt == 4:
                    print("All filters has been removed")
                    data = dataOri
                    activeFilt = np.zeros(6)
                #Quits the filter 
                elif filt == 5:
                    break
        else:
            print("No data has been loaded\n")
            
    #Calls the data statistics funtion
    elif choice == 3:
        if data != []:
            #Displays menu with options for statistics
            opt = misc.displayMenu(statOptions)
            optStat = statOptionsDict[opt]
            print("{}: {}".format(optStat,bda_lib.dataStatistics(data,optStat)))
        else:
            print("No data has been loaded\n")
        
    #Plots data
    elif choice == 4:
        if data !=[]:
            bda_lib.dataPlot(data)
        else:
            print("No data has been loaded\n")
            
    #Quits the program  
    elif choice == 5:
        print("Quitting... Have a nice day")
        sleep(2)
        break
