import numpy as np
import sys
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Convolution1D, Convolution2D, MaxPooling2D, MaxPooling1D, ZeroPadding2D, AveragePooling2D, Activation
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from keras import optimizers
import keras.backend as K
from keras.callbacks import LearningRateScheduler, EarlyStopping, ModelCheckpoint


def predict(csv_filepath):
    data = pd.read_csv(csv_filepath)
    data = data.drop(['Flow ID', 'Src IP', 'Dst IP', 'Src Port',
                      'Dst Port', 'Timestamp', 'Label'], axis=1)
    data = np.expand_dims(data, axis=2)
    model = load_model("./model/model-00006-0.98196-0.06294.h5")
    # model2 = load_model(sys.argv[2])
    # model3 = load_model(sys.argv[3])
    # model4 = load_model(sys.argv[4])
    pred = 0.0
    pred += model.predict(data)
    # pred += model2.predict(data)
    # pred += model3.predict(data)
    # pred += model4.predict(data)
    # pred = result/4
    print(pred.shape)
    print(pred)
    return pred


data = "./data/output-4/pornhub1.pcap_Flow.csv"
predict(data)
