import numpy as np

def inputNumber(prompt):
    #Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    #Takes input and checks that is is an integer, if it is not, keeps asking for input
    
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Not a valid entry")
            pass

    return num

def displayMenu(options):
    #Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    #Displays menu with the options in the input array

    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0

    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")

    print("")   # new line

    return choice

def printFilter(filter_array):
    #Takes an array six long, with information on curently applied filters
    #If no filters are applied outputs nothing
    
    msg = []
    if filter_array[0]==1:
        msg.append("Salmonella enterica removed")
    if filter_array[1]==1:
        msg.append("Bascillus cereus removed")
    if filter_array[2]==1:
        msg.append("Listeria removed")
    if filter_array[3]==1:
        msg.append("Brochothtrix thermosphacta removed")
    if filter_array[4]!=0:
        msg.append("Upper Bound: {}".format(filter_array[4]))
    if filter_array[5]!=0:
        msg.append("Lower Bound: {}".format(filter_array[5]))
    if np.sum(filter_array)!=0:    
        print("Active filters:", ", ".join(str(s) for s in msg), "\n")
    
    
