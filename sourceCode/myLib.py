import numpy as np

#TODO load du lieu tu file scv do vao mot numpy.array

def loadData(scvFile):
    return np.loadtxt(scvFile, delimiter=',')

#TODO so sanh ket qua voi nhan trong tap ctu 13 goc

def compairResultvsTestLabel(filepath):
    resultFile = open(filepath, 'r')
    testLabelFile = open('data/testLabel.csv', 'r')
    result = loadData(resultFile)
    testLabel = loadData(testLabelFile)
    count = 0 #so luong ket qua chinh xac
    botnetFl = 0 #so luong flow botnet
    resultBotFl = 0 #so luong flow botnet phat hien chinh xac
    for i in range(0, result.shape[0]):
        if(testLabel[i] == 1):
             botnetFl += 1
             if (result[i] == 1):
                 resultBotFl += 1
        if(np.array_equal(result[i], testLabel[i])):
            count += 1
    print('so netflow gan nhan botnet:' + str(botnetFl))
    print('so netflow botnet nhan dien chinh xac: '+ str(resultBotFl))
    print('so netflow nhan dien chinh xac: ' + str(count))
    print('ti le nhan dien botnet:' + str(resultBotFl/botnetFl * 100) + '%')
    print('ti le chinh xac:' + str(count/result.shape[0] * 100)+ '% ')
    resultFile.close()
    testLabelFile.close()