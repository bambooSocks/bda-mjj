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
