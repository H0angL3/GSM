''' su dung mo hinh knn de train
created by: Hoang Le
'''
import numpy as np
import csv
from sklearn import neighbors
import pickle
from src.myLib import *

def KNN():
    trainFile = open('data/train.csv', 'rb')
    inputTrain = loadData(trainFile)
    trainFile.close()
    labelFile = open('data/trainLabel.csv', 'rb')
    label = loadData(labelFile)
    labelFile.close()
    print('data load: done')
    print('begin training KNN')
    clf = neighbors.KNeighborsClassifier()
    clf.fit(inputTrain, label)
    print('training bayes: done')
    fileSvc = 'model/KNN_final.sav'
    pickle.dump(clf, open(fileSvc, 'wb'))
    print('save model done')

def testKNN():
    clf = pickle.load(open('model/KNN_final.sav', 'rb'))
    testData = loadData('data/test.csv')
    resultFile = open('data/resultTestKNN.csv', 'w')
    print('tai xong du lieu')
    inwr = csv.writer(resultFile)
    for data in testData:
        result = [int(clf.predict(np.array([data])))]
        inwr.writerow(result)
    resultFile.close()


#training
# KNN()
testKNN()
print('ket qua thuat toan KNN')
evaluateModel('data/resultTestKNN.csv', 'data/testLabel.csv')
