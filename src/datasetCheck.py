import numpy as np
import csv
from imblearn.combine import SMOTEENN
#TODO load du lieu tu file scv do vao mot numpy.array

def loadData(scvFile):
    return np.loadtxt(scvFile, delimiter=',')

capfile = 'data/trainLabel.csv'
trainLabel = loadData(capfile)

neiv = 0
posi = 0
shape = trainLabel.shape[0]
for i in range (0, shape):
    if (trainLabel[i]==0):
        neiv += 1
    if (trainLabel[i] == 1):
        posi += 1
info = [posi, neiv, shape ,posi/(shape), neiv/posi]
print(info)


