'''xu li du lieu netflow trong ctu 13
lua chon cac dan trung sau: SPort,DPort, DAddress,bytePerPkt, avgByte = totalByte/duration, avgPkt = totalPKTs/duration, label
xu li du lieu trong cac file ctu: 1, 3, 4, 5 --> training set:
    input  {SPort,DPort, bytePerPkt ,avgPkt, avgByte}
    output {label (da xy li)} ::: label co 2 loai: normal va botnet
xu li du lieu trong cac file 2, 11 --> testing set {SPort,DPort, bytePerPkt ,avgPkt, avgByte}

created  by : Hoang Le
'''
import csv
#TODO xu li file dau vao
def dataPrepocess(filename, fileInputSet, fileOutputSet):
    with open(filename) as file:
        contentFile = file.readlines()
    del contentFile[0]
    inputSet = open(fileInputSet, 'w+')
    outputSet = open(fileOutputSet, 'w+')
    inwr = csv.writer(inputSet)
    outwr = csv.writer(outputSet)
    for flow in contentFile:
        listFlow = flow.split(',')
        dur = float(listFlow[1])
        if (dur != 0):
            try:
                data = [int(listFlow[4].strip()), int(listFlow[7].strip()), float(listFlow[12])/float(listFlow[11]),float(listFlow[11])/dur, float(listFlow[12])/dur]
                inwr.writerow(data)

                if('Botnet' in listFlow[14]):
                    outwr.writerow([1]) #1 is bonet and 0 is normal
                else:
                    outwr.writerow([0])
            except:
                print('flow bi loi:' + flow)

    inputSet.close()
    outputSet.close()

# xu li du lieu cho test data va train data

dataPrepocess('data_raw/test.txt', 'data/trainInSet.csv', 'data/trainOutSet.csv')

