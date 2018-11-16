''' su dung mo hinh naive bayes de train
created by: Hoang Le
'''
import csv
import numpy as np
from sklearn import model_selection
from sklearn.svm import SVC
import pickle
#TODO load du lieu tu file scv
def loadData(scvFile):
    return np.loadtxt(scvFile, delimiter=',')

def svm():
    trainFile = open('data/train.csv', 'rb')
    inputTrain = loadData(trainFile)
    trainFile.close()
    labelFile = open('data/trainLabel.csv', 'rb')
    label = loadData(labelFile)
    labelFile.close()
    print('data load: done')
    print('begin training')
    clf = SVC(gamma='auto')
    clf.fit(inputTrain, label)
    print('training: done')
    fileSvc = 'model/svc_final.sav'
    pickle.dump(clf, open(fileSvc, 'wb'))
    print('save model done')

def testSvm():
    clf = pickle.load(open('model/svc_final.sav', 'rb'))
    testData = loadData('data/test.csv')
    resultFile = open('data/resultTestSVM.csv', 'w')
    inwr = csv.writer(resultFile)
    for data in testData:
        result = [int(clf.predict(np.array([data])))]
        inwr.writerow(result)
    resultFile.close()



def compairResultvsTestLabel():
    resultFile = open('data/resultTestSVM.csv', 'r')
    testLabelFile = open('data/testLabel.csv', 'r')
    result = loadData(resultFile)
    testLabel = loadData(testLabelFile)
    print(result.shape)
    print(testLabel.shape)
    count = 0
    for i in range(0, result.shape[0]):
        if(np.array_equal(result[i], testLabel[i])):
            count += 1
    print(count)
    print(str(count/result.shape[0] * 100)+ '% ')

testSvm()