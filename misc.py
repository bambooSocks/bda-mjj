import numpy as np

def inputNumber(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Not a valid entry")
            pass

    return num

def displayMenu(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")

    return choice

def printFilter(fA):
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
    
    
