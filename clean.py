# clean data 

import numpy as np
import pandas as pd
from dload import all_data
import math

# check NAs
all_data.isnull().sum()

# split into train, test, validate
test_size=.8
num_rows=all_data.shape[0]
split=math.floor(test_size*num_rows)

train=all_data[1:split]
test=all_data[split:]


### TAKING OUT VALIDATION DATA BECAUSE KERAS CAN DO IT

# train_rows=train.shape[0]
# train_split=math.floor(test_size*train_rows)

# valid=train[train_split:]
# train=train[1:train_split]

# prepare train, test, valid data for keras

# remove non needed rows. in this case, drop movement variable
train = train.drop('movement', 1)
# valid = valid.drop('movement', 1)
test = test.drop('movement', 1)

# split labels of from training set
train_label, test_label = 	train.pop('gain_loss'), test.pop('gain_loss')


# convert labels to one hots and np with get dummies
train_label, test_label = pd.get_dummies(train_label), pd.get_dummies(test_label)
train_label, test_label = train_label.values, test_label.values, 

# convert train to np
train, test = train.values, test.values




# imput and rescale features
from sklearn import preprocessing
from sklearn.preprocessing import Imputer

# fill in missing values in features, using mean strategy
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
fittx=imp.fit(train)
# fity=imp.fit(valid)
fitz = imp.fit(test)

train, test =imp.transform(train), imp.transform(test)

train, test = preprocessing.scale(train), preprocessing.scale(test)


# reshape for keras LSTM
#need  [samples, time steps, features]. 
# Currently, our data is in the form: [samples, features] 
# and we are framing the problem as one time step for each sample. 
train = np.reshape(train, (train.shape[0], train.shape[1],1))
# valid = np.reshape(valid, (valid.shape[0], valid.shape[1],1))
test = np.reshape(test, (test.shape[0], test.shape[1],1))

