import numpy as np
import math

def dataStatistics(data,stat):
    a=0
    b=0

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
        for id in data:
            if id[0]>20:
                a +=id[1]
                b +=1
        results=a/b

    elif stat == 'Mean Hot Growth rate':
        for id in data:
            if id[0]<50:
                a+=id[1]
                b+=1
        results=a/b

    return results

def dataLoad(filename):
    # Insert your code here
    data=open(filename)
    data = data.readlines()
    rows=math.ceil(np.size(data))
    data=np.reshape(data,[rows,1])
    return data
