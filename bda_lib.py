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
    data=np.array([])
    #3rd row posiible values
    values=np.array([1,2,3,4])
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                data=np.hstack((data,np.array(float(word))))
    rows=math.ceil(np.size(data)/3)
    data=np.reshape(data,[rows,3])
    correctrows_number=0
    for i in range(rows):
        row=data[i,:]
        errorcounter=0
        if (row[0]>60 or row[0]<10):
            errorcounter=errorcounter+1
        if (row[1]<=0):
            errorcounter=errorcounter+1
        column3=values[values==row[2]]
        if (np.size(column3)!=1):
            errorcounter=errorcounter+1
        if errorcounter==0:
            correctrows_number=correctrows_number+1
            if correctrows_number==1:
                correctdata=row
            elif correctrows_number>1:
                correctdata=np.vstack((correctdata,row))
    data=correctdata
    return data
