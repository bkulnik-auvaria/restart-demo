import numpy as np
file=open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\02-CSV\data.csv','r')
dat=file.readlines()
ls=[]
for x in dat:
    ls.append(float(x.split(',')[1]))

print(np.mean(ls))