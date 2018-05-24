import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import sys
import os

#aaa = pd.read_csv("/home/ganlinya/下載/csv output/ftps_up_2a.pcap_Flow.csv")
#bbb = pd.read_csv("/home/ganlinya/下載/csv output/netflix2.pcap_Flow.csv")
#print(bbb['Flow Duration'])
#bbb.sort(key = lambda x: x['Timestamp'])
def matplotgen(aaa,name):
    t = name
    df = [[],[]]
    see = aaa['TotLen Fwd Pkts']
    for i in range(len(aaa['Timestamp'])) :
        tmp=0
        tmp2=0

        for j in range(11,13):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;
        for j in range(14,16):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;
        for j in range(17,19):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;

        df[0].append(tmp)

        df[1].append(float(see[i]) )

    df2 = [[],[]]
    see = aaa['TotLen Bwd Pkts']
    for i in range(len(aaa['Timestamp'])) :
        tmp=0
        tmp2=0
        for j in range(11,13):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;
        for j in range(14,16):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;
        for j in range(17,19):
            tmp2=tmp2*10 + int(aaa['Timestamp'][i][j])
        tmp=60*tmp+tmp2;
        tmp2=0;
        df2[0].append(tmp)
        lasttime = tmp
        df2[1].append(float(see[i]))

    #print(df)
    a=0
    h = []
    df[0],df[1] = (list(t) for t in zip(*sorted(zip(df[0],df[1]))))
    df2[0],df2[1] = (list(t) for t in zip(*sorted(zip(df2[0],df2[1]))))



    plt.subplot(1,2,1)
    plt.bar(df[0],df[1],color = 'red')
    plt.title(t)
    plt.xlabel('time')
    plt.ylabel('Totlen Fwd Pkts')
    plt.subplot(1,2,2)
    plt.bar(df[0],df2[1],width = 200)
    plt.xlabel('time')
    plt.ylabel('Totlen Bwd Pkts')
    #plt.show()
    plt.savefig(name + '.png')
    plt.close()



csv_list = glob.glob("/Users/brandon/Desktop/project/csv output/*.csv")
i = 0
for csv in csv_list:
    b = os.path.splitext(csv)
    b = str(b[0])
    d = b.split("/")
    name = (d[-1])
    print(name)
    c = pd.read_csv(csv)
    matplotgen(c,name)
