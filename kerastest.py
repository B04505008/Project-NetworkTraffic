import numpy as np
import sys
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Convolution2D, MaxPooling2D, ZeroPadding2D, AveragePooling2D, Activation
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.datasets import mnist
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


def model(x_train, y_train, x_test, y_test):
    model = Sequential()
    model.add(Dense(input_dim=8, units=1024, activation='relu'))
    #model.add(Dropout(0.3))
    model.add(Dense(units=1024, activation='relu'))
    #model.add(Dropout(0.3))
    for i in range(8):
        model.add(Dense(units=2048, activation='relu'))
        #model.add(Dropout(0.3))

    model.add(Dense(units=1, activation='sigmoid'))
    #Configuration
    #opt = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    #opt = optimizers.SGD(lr=0.01)
    #model.compile(loss = "mean_squared_error", optimizer = opt, metrics=['accuracy'])
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    #model.compile(loss='kullback_leibler_divergence', optimizer='adam', metrics=['accuracy'])
    #Pick the best function
    train_history = model.fit(
        x_train, y_train, validation_split=0.2, batch_size=128, epochs=512, verbose=2)

    result = model.evaluate(x_train, y_train, batch_size=10000)
    print("train accuracy:", result[1])

    result = model.evaluate(x_test, y_test, batch_size=10000)
    print("test accuracy:", result[1])
    return train_history

def load_data():
    train = pd.read_csv("./train.csv")
    test = pd.read_csv("./test.csv")
    x_train = train.drop(["vpn"], axis=1)
    y_train = train["vpn"]
    x_test = test.drop(["vpn"], axis=1)
    y_test = test["vpn"]
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    '''y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    x_train /= 255
    x_test /= 255'''
    #print("y_train:",y_train)
    return (x_train, y_train), (x_test, y_test)

def sigmoid(z):
    out = 1 / (1.0 + np.exp(-z))
    return out

def nor(x_train, x_test):
    for i in range(x_train.shape[1]):
        mean = np.mean(x_train.iloc[:, i])
        std = np.std(x_train.iloc[:, i])
        mmax = np.max(x_train.iloc[:, i])
        print (i,"'s mean,std",mean,std,mmax)
        #x_train = (x_train - mean) / (std + 1e-15)
        #x_test = (x_test - mean) / (std + 1e-15)
        x_train = np.arctan(x_train)*2 / np.pi
        x_test = np.arctan(x_test)*2 / np.pi
    return x_train, x_test


(x_train, y_train), (x_test, y_test) = load_data()
#x_train, x_test = nor(x_train, x_test)
x_train = np.array(x_train, dtype=np.long)
x_test = np.array(x_test, dtype=np.long)
x_train = preprocessing.scale(x_train)
x_test = preprocessing.scale(x_test)
#min_max_scaler = preprocessing.MinMaxScaler()
#X_train_minmax = min_max_scaler.fit_transform(x_train.as_matrix())
#X_test_minmax = min_max_scaler.fit_transform(x_test)
#scaler = StandardScaler()
#x_test = scaler.fit(x_test)
train_history = model(x_train, y_train, x_test, y_test)

show_train_history(train_history, 'acc', 'val_acc')
show_train_history(train_history, 'loss', 'val_loss')
