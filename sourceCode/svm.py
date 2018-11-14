''' su dung mo hinh naive bayes de train
created by: Hoang Le
'''
import numpy as np
from sklearn import model_selection
from sklearn.svm import SVC
import pickle
#TODO load du lieu tu file scv
def loadData(scvFile):
    return np.loadtxt(scvFile, delimiter=',')

def svm():
    inputTrain = loadData('data/trainInSet.csv')
    label  = loadData('data/trainOutSet.csv')
    clf = SVC(gamma='auto')
    clf.fit(inputTrain, label)
    fileSvc = 'model/svc_final.sav'
    pickle.dump(clf, open(fileSvc, 'wb'))

def testSvm(test):
    clf = pickle.load(open('model/svc_final.sav', 'rb'))
    print(clf.predict(test))


