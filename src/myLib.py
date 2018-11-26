import numpy as np

#TODO load du lieu tu file scv do vao mot numpy.array

def loadData(scvFile):
    return np.loadtxt(scvFile, delimiter=',')

#TODO so sanh ket qua voi nhan trong tap ctu 13 goc

def evaluateModel(filepath, respath):
    resultFile = open(filepath, 'r')
    testLabelFile = open(respath, 'r')
    result = loadData(resultFile)
    testLabel = loadData(testLabelFile)
    shape = result.shape[0]
    acc = 0 #so luong ket qua chinh xac
    positive = 0 #so luong flow botnet (duongtinh)
    truePositive = 0
    negative = 0 #so luowng normarl (am tinh)
    trueNegative = 0
    for i in range(0, result.shape[0]-1):
        #tinh acc
        if(np.array_equal(result[i], testLabel[i])):
            acc += 1
        #tinh positive
        if(result[i] == 1):
            positive += 1
            if(testLabel[i] == 1):
                truePositive += 1
        if(result[i] == 0):
            negative += 1
            if(testLabel[i]==0):
                trueNegative += 1
    falseNegative = negative - trueNegative
    print('so luong netflow: ' + str(shape))
    print('so luong flow gan nhan chinh xac: ' + str(acc))
    print('so luong flow botnet (positive):' + str(truePositive + falseNegative))
    print('ti le chinh xac Accuracy:' + str(acc / shape * 100) + '% ')
    print('so luong flow botnet gan nhan chinh xac: ' + str(truePositive))
    print('ti le chinh xac Precision:' + str((truePositive/positive) * 100) + '%')
    print('ti le Recall: ' + str((truePositive/(truePositive + falseNegative)) * 100) + '%')
    resultFile.close()
    testLabelFile.close()