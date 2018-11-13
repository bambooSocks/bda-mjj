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
    
    print("\n")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")

    return choice

def printFilter(fA):
    #Takes an array six long, with information on curently applied filters
    #If no filters are applied outputs nothing
    
    msg = []
    if fA[0]==1:
        msg.append("Salmonella enterica")
    if fA[1]==1:
        msg.append("Bascillus cereus")
    if fA[2]==1:
        msg.append("Listeria")
    if fA[3]==1:
        msg.append("Brochothtrix thermosphacta")
    if fA[4]!=0:
        msg.append("Upper Bound: {}".format(fA[4]))
    if fA[5]!=0:
        msg.append("Lower Bound: {}".format(fA[5]))
    if np.sum(fA)!=0:    
        print("Active filters:",msg)
    
    
