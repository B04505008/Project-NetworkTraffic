import sys
import pandas as pd
import glob
import csv
import os
from sklearn.utils import shuffle

def sort(file,name):
    copy = file.drop(['Flow ID', 'Src IP', 'Dst IP',
                      'Timestamp', 'Label'], axis=1)
    #copy = copy[['Src Port', 'Dst Port', 'Bwd IAT Mean','Idle Max', 'Fwd IAT Min', 'Idle Min', 'Flow Byts/s', 'Flow IAT Std']]
    #copy = copy['Src Port']
    if name.find("tor") != -1:
        print("find a tor protocol")
        copy["tor"] = 1
    else:
        copy["tor"] = 0
        print("find a non-tor protocol")
    #print(copy)
    return copy



csv_list = glob.glob("/Users/brandon/Desktop/project/csv output/*.csv")
i = 0
for csv in csv_list:
    b = os.path.splitext(csv)
    b = str(b[0])
    d = b.split("/")
    name = (d[-1])
    print(name)
    c = pd.read_csv(csv)
    newcsv = sort(c,name)
    i += 1
    print(i,"csv file has been sorted")
    if i ==1 :
        newcsv.to_dense().to_csv("ans_tor.csv", index=False, sep=',', encoding='utf-8')
    else:
        newcsv.to_dense().to_csv("ans_tor.csv", index=False, sep=',', encoding='utf-8', header=False, mode='a+')
    print("file was added successuflly")

file = pd.read_csv("./ans_tor.csv")
shuffle(file).to_dense().to_csv("ans_tor.csv", index=False, sep=',', encoding='utf-8')
