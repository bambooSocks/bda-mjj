import numpy as np
from time import sleep
import misc
import bda
import os.path

# Global variables
# all main menu options
main_menu = np.array(["Load Data", "Filter Data", "Display Statistics", "Generate Plots", "Quit"])
# dictionary storing all statistics menu options
stat_menu_dict = { 1 :'Mean Temperature', 2 :'Mean Growth rate', 3 :'Std Temperature', 4 :'Std Growth rate',
				   5 :'Rows', 6 :'Mean Cold Growth rate', 7 :'Mean Hot Growth rate'}
# all filter menu options
filter_menu = np.array(["Apply Bacteria Filter", "Apply Upper Growth Rate Filter", "Apply Lower Growth Rate Filter", 
            	"Clear Filters", "Quit Filter Menu"])
# list of bacterias for filtering
bacteria_menu = np.array(["Salmonella enterica", "Bascillus cereus", "Listeria", "Brochothtrix thermosphacta"])
orig_data = []					# originaly loaded data for recovery
current_data = []				# currently loaded data with applied filters
active_filter = np.zeros(6)		# active data filters

# Main Loop
while True:
    
    misc.printFilter(active_filter)
    choice = misc.displayMenu(main_menu)
    
    # Calls the dataLoad function
    if choice == 1:
        print("Your data file should be in the same directory as this script")
        filename = input("Input file name: ")
        print("")
        # Checks if the file exists
        if os.path.exists(filename):
        	# if it does load the data
            orig_data = bda.dataLoad(filename)
            current_data = orig_data
        else:
            print("File does not exist\n")
        
    # Applies filters
    elif choice == 2:
    	# filter menu loop
        while True:
            misc.printFilter(active_filter)
            filt = misc.displayMenu(filter_menu)
            # Bacteria filters
            if filt == 1 and np.size(current_data) != 0:
                print("Exclude bacteria type:")
                chosen_filter = misc.displayMenu(bacteria_menu)
                # removes data of chosen bacteria from current data buffer
                current_data = current_data[current_data[:,2] != chosen_filter]
                active_filter[chosen_filter-1] =1
            # Upper growth rate bound filter
            elif filt == 2 and np.size(current_data) != 0:
                chosen_filter = float(input("Input upper bound: "))
                # removes all the data outside of the bounds
                current_data = current_data[current_data[:,1] <= chosen_filter]
                active_filter[4] = chosen_filter
            # Lower growth rate bound filter
            elif filt == 3 and np.size(current_data) != 0:
                chosen_filter = float(input("Input lower bound: "))
                # removes all the data outside of the bounds
                current_data = current_data[current_data[:,1] >= chosen_filter]
                active_filter[5] = chosen_filter
            # Clears all filters
            elif filt == 4:
                print("All filters has been removed\n")
                # reloading the original data and clearing the filter mask
                current_data = orig_data
                active_filter = np.zeros(6)
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
            stat_menu = np.array(list(stat_menu_dict.values()))
            opt = misc.displayMenu(stat_menu)

            optStat = stat_menu_dict[opt]
            print("{}: {}\n".format(optStat, bda.dataStatistics(current_data, optStat)))
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
