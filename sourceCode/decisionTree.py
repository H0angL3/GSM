''' su dung mo hinh naive bayes de train ids
created by: Hoang Le
'''
import numpy as np
import csv
from sklearn import tree
import pickle
from src.myLib import *
def decisionTree():
    trainFile = open('data/train.csv', 'rb')
    inputTrain = loadData(trainFile)
    trainFile.close()
    labelFile = open('data/trainLabel.csv', 'rb')
    label  = loadData(labelFile)
    labelFile.close()
    print('data load: done')
    print('begin training bayes')
    clf = tree.DecisionTreeClassifier()
    clf.fit(inputTrain, label)
    print('training bayes: done')
    fileSvc = 'model/decision_tree.sav'
    pickle.dump(clf, open(fileSvc, 'wb'))
    print('save model done')

def testDecisionTree():
    clf = pickle.load(open('model/decision_tree.sav', 'rb'))
    testData = loadData('data/test.csv')
    resultFile = open('data/resultTestDecTree.csv', 'w')
    print('tai xong du lieu')
    inwr = csv.writer(resultFile)
    for data in testData:
        result = [int(clf.predict(np.array([data])))]
        inwr.writerow(result)
    print('test xong. Ket qua luu trong data/resultTestDecTree.csv')
    resultFile.close()

#training
print('thuat toan cay quyet dinh')
decisionTree()
testDecisionTree()
compairResultvsTestLabel('model/decision_tree.sav')