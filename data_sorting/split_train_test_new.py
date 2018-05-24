import sys
import pandas as pd
import csv
import os
from sklearn.utils import shuffle

inputcsv = sys.argv[1]
traincsv = sys.argv[2]
testcsv = sys.argv[3]


file = pd.read_csv(inputcsv)
print("file data shape",file.shape[0],file.shape[1])


file.iloc[[0]].to_dense().to_csv(traincsv, index=False, sep=',', encoding='utf-8')
file.iloc[[0]].to_dense().to_csv(testcsv, index=False, sep=',', encoding='utf-8')
for i in range(file.shape[0]+1):
    if i < 0.7 * file.shape[0]:
        file.iloc[[i+1]].to_dense().to_csv(traincsv, index=False, sep=',', encoding='utf-8', header=False, mode='a+')
    else:
        file.iloc[[i+1]].to_dense().to_csv(testcsv, index=False, sep=',', encoding='utf-8', header=False, mode='a+')
