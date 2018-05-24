import sys
import pandas as pd
import glob
import csv
import os
from sklearn.utils import shuffle

'''inputcsv1 = pd.read_csv(sys.argv[1], low_memory=False)
inputcsv2 = pd.read_csv(sys.argv[2], low_memory=False)
csvlist = [inputcsv1, inputcsv2]
result = pd.concat(csvlist)
result.to_csv("combine.csv")'''

file = pd.read_csv("./train.csv", low_memory=False)
shuffle(file).to_dense().to_csv("train.csv", index=False, sep=',', encoding='utf-8')
