import numpy as np
import math

def dataStatistics(data,stat):

    if stat == 'Mean Temperature':
        results=np.average(data[:,0])

    elif stat == 'Mean Growth rate':
        results=np.average(data[:,1])

    elif stat == 'Std Temperature':
        results=np.std(data[:,0])

    elif stat == 'Std Growth rate':
        results=np.std(data[:,1])

    elif stat == 'Rows':
        results=np.size(data,0)

    elif stat == 'Mean Cold Growth rate':
        results = np.average(data[data.T[0]>20].T[1])
        
    elif stat == 'Mean Hot Growth rate':
        results = np.average(data[data.T[0]<50].T[1])
        
    return results


def dataLoad(filename):

    matrix = np.array([]) # This variable will consist of data from txt

    with open(filename,'r') as f: # opening file
        for line in f: # changing file into an array containing values exept strings
            for word in line.split():
                matrix = np.hstack((matrix, np.array(float(word))))

    rows = math.ceil(np.size(matrix)/3) # finding number of rows
    matrix = np.reshape(matrix,[rows,3])
    correct = 0 # number of correct rows

    for i in range(rows): # checking statements for every row

        row = matrix[i,:]
        err=np.array([]) # this array will contain every type of error in line

        if (row[0] > 60 or row[0] < 10): # Statement for temperature error
            err = np.concatenate((err, ['Temperature']))

        if (row[1] <= 0): # Statement for growth rate error
            err=np.concatenate((err, ['Growth rate']))

        if(row[2] < 1 or row[2] > 4 or ((row[2]).is_integer() == False)):
            err = np.concatenate((err, ['Bacteria']))

        if np.size(err) == 0:
            correct += 1
            if correct == 1:
                data = row
            elif correct > 1:
                data = np.vstack((data,row))

        else:
            print("Error(s) in line {}: {}.".format(i+1, ", ".join(str(e) for e in err)) )

    return data
