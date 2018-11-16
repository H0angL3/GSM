'''xu li du lieu netflow trong ctu 13
lua chon cac dan trung sau: srcIP,srcPort, dstIP, dstPort, state, sTOS,
        bytePerPkt, avgByte = totalByte/duration, avgPkt = totalPKTs/duration, label
xu li du lieu trong cac file ctu: 1, 3, 4, 5 --> training set:
    input  {srcIP, srcPort, state,sTOS, srcPort, bytePerPkt ,avgPkt, avgByte}
    output {label (da xy li)} ::: label co 2 loai: normal va botnet
xu li du lieu trong cac file 2, 6 --> testing set
khong xu li mot so loai netflow nhu ipv6-icmp
created  by : Hoang Le
'''
import csv
from src.dataPrepLib import *

#TODO xu li file dau vao
def dataPrepocess(filename, fileInputSet, fileOutputSet):
    with open(filename) as file:
        contentFile = file.readlines()
    del contentFile[0]
    inwr = csv.writer(fileInputSet)
    outwr = csv.writer(fileOutputSet)
    for flow in contentFile:
        data, label = flowToArray(flow)
        if(data != -1 and label != -1):
            inwr.writerow(data)
            outwr.writerow(label)
# xu li du lieu cho test data va train data
def trainDataPrepocess():
    trainFile = open('data/train.csv','w+')
    trainLabel = open('data/trainLabel.csv','w+')
    dataPrepocess('data_raw/cap1.binetflow',trainFile, trainLabel)
    dataPrepocess('data_raw/cap3.binetflow', trainFile, trainLabel)
    dataPrepocess('data_raw/cap4.binetflow', trainFile, trainLabel)
    dataPrepocess('data_raw/cap5.binetflow', trainFile, trainLabel)
    trainFile.close()
    trainLabel.close()

def testDataPrepocess():
    testFile = open('data/test.csv', 'w+')
    testLabel = open('data/testLabel.csv', 'w+')
    dataPrepocess('data_raw/cap11.binetflow', testFile, testLabel)
    dataPrepocess('data_raw/cap9.binetflow', testFile, testLabel)
    testFile.close()
    testLabel.close()

