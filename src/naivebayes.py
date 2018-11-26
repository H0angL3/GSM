''' su dung mo hinh naive bayes de train
created by: Hoang Le
'''
import numpy as np
import csv
from sklearn.naive_bayes import GaussianNB
import pickle
from src.myLib import *
#TODO train with Gaussian navie bayes model
#luu model vao file 'model/bayes_final.sav'
def naiveBayes():
    trainFile = open('data/train.csv', 'rb')
    inputTrain = loadData(trainFile)
    trainFile.close()
    labelFile = open('data/trainLabel.csv', 'rb')
    label  = loadData(labelFile)
    labelFile.close()
    print('data load: done')
    print('begin training bayes')
    clf = GaussianNB()
    clf.fit(inputTrain, label)
    print('training bayes: done')
    # luu model sau khi train
    fileSvc = 'model/bayes_final.sav'
    pickle.dump(clf, open(fileSvc, 'wb'))
    print('save model: done')

def testBayes():
    print('begin test:....')
    #tai model tu bayes_final.sav
    clf = pickle.load(open('model/bayes_final.sav', 'rb'))
    testData = loadData('data/test.csv')
    resultFile = open('data/resultTestBayes.csv', 'w')
    print('tai xong du lieu')
    inwr = csv.writer(resultFile)
    for data in testData:
        result = [int(clf.predict(np.array([data])))]
        inwr.writerow(result)
    print('test: done')
    print('ket qua luu tai: data/resultTestBayes.csv')
    resultFile.close()


#training
# naiveBayes()
testBayes()
evaluateModel('data/resultTestBayes.csv', 'data/testLabel.csv')
