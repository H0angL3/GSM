import ipaddress
import numpy as np
#TODO convert IPv4 to int
def ipToInt(ipv4):
    return int(ipaddress.IPv4Address(ipv4))

#TODO convert state in netflow to int
'''
ham nay thuc thi theo huong dan decode flag netflow
theo link:  https://www.manitonetworks.com/flow-management/2016/10/16/decoding-tcp-flags
input = state
output = int
'''

def stateToInt(state):
    dicFlag = {'CON': 128, 'INT': 64, 'U': 32, 'A': 16, 'P': 8, 'R': 4, 'S': 2, 'F': 1}
    if (state == 'CON'):
        return dicFlag['CON']
    elif (state == 'INT'):
        return dicFlag['INT']
    else:
        encode = 0
        flagList = list(state)
        for flag in flagList:
            if flag in dicFlag:
                encode += dicFlag[flag]
            else:
                encode += 0
        return encode


#TODO convert netflow in CTU 13 to data with 9 feture and label
#input  = netfolw
#output  data = [sPort, dIp, dPort, state, sTos, bytePerPkt, avgPkt, avgByte]
#and label = [0 or 1]
def flowToArray(flow):
    listFlow = flow.split(',')
    dur = float(listFlow[1])
    if (dur != 0):
        try:
            dIp = ipToInt(listFlow[6])
            state = stateToInt(listFlow[8])
            bytePerPkt = float(listFlow[12]) / float(listFlow[11])
            avgPkt = float(listFlow[11]) / dur
            avgByte = float(listFlow[12]) / dur
            if (listFlow[9] == ''):
                sTos = 0
            else:
                sTos = int(listFlow[9])
            # goi tin icmp khong co port => gan dstport = 0 ang srcport = 0
            if (listFlow[2] == 'icmp'):
                data = [0, dIp, 0, state, sTos, bytePerPkt, avgPkt, avgByte]
            # goi tin icmp khong co port => gan dstport = 1 ang srcport = 1
            elif (listFlow[2] == 'arp'):
                data = [1, dIp, 1, state, sTos, bytePerPkt, avgPkt, avgByte]
            #doi tin esp
            elif (listFlow[2] == 'esp'):
                data = [2, dIp, 2, state, sTos, bytePerPkt, avgPkt, avgByte]
            #goi tin tcp khong co dstport
            elif (listFlow[2] == 'tcp' and listFlow[7] == ''):
                data = [int(listFlow[4].strip()), dIp, 3, state, sTos, bytePerPkt, avgPkt, avgByte]
            #goi tin igmp
            elif (listFlow[2] == 'igmp'):
                data = [4, dIp, 4, state, sTos, bytePerPkt, avgPkt, avgByte]
            else:
                data = [int(listFlow[4].strip()), dIp, int(listFlow[7]), state, sTos, bytePerPkt, avgPkt, avgByte]
            if ('Botnet' in listFlow[14]):
                label = [1]  # 1 is bonet and 0 is normal
            else:
                label = [0]
            return data, label
        except:
            print('khong xu li duoc: ' + flow)
            return (-1, -1)
    else:
        try:
            dIp = ipToInt(listFlow[6])
            state = stateToInt(listFlow[8])
            bytePerPkt = float(listFlow[12]) / float(listFlow[11])
            avgPkt = listFlow[11]
            avgByte = listFlow[12]
            if (listFlow[9] == ''):
                sTos = 0
            else:
                sTos = int(listFlow[9])
            # goi tin icmp khong co port
            if (listFlow[2] == 'icmp'):
                data = [0, dIp, 0, state, sTos, bytePerPkt, avgPkt, avgByte]
            # goi tin khong co port dich: arp, esp,.... dport = 55555
            elif (listFlow[2] == 'arp'):
                data = [1, dIp, 1, state, sTos, bytePerPkt, avgPkt, avgByte]
            elif (listFlow[2] == 'esp'):
                data = [2, dIp, 2, state, sTos, bytePerPkt, avgPkt, avgByte]
            elif (listFlow[2] == 'tcp' and listFlow[7] == ''):
                data = [int(listFlow[4].strip()), dIp, 3, state, sTos, bytePerPkt, avgPkt, avgByte]
            elif (listFlow[2] == 'igmp'):
                data = [4, dIp, 4, state, sTos, bytePerPkt, avgPkt, avgByte]
            else:
                data = [int(listFlow[4].strip()), dIp, int(listFlow[7]), state, sTos, bytePerPkt, avgPkt, avgByte]
            if ('Botnet' in listFlow[14]):
                label = [1]  # 1 is bonet and 0 is normal
            else:
                label = [0]
            return data, label
        except:
            print('khong xu li duoc: ' + flow)
            return (-1, -1)



