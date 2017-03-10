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

train_rows=train.shape[0]
train_split=math.floor(test_size*train_rows)

valid=train[train_split:]
train=train[1:train_split]

# prepare train, test, valid data for keras

# remove non needed rows. in this case, drop movement variable
train = train.drop('movement', 1)
valid = valid.drop('movement', 1)
test = test.drop('movement', 1)

# split labels
train_label, valid_label, test_label = 	train.pop('gain_loss'),valid.pop('gain_loss'),test.pop('gain_loss')


# convert labels to one hots and np with get dummies?
train_label, valid_label, test_label = pd.get_dummies(train_label), pd.get_dummies(valid_label), pd.get_dummies(test_label)
train_label, valid_label, test_label = train_label.values, valid_label.values, test_label.values, 

# convert train to np
train, valid, test = train.values, valid.values, test.values




# imput and rescale features
from sklearn import preprocessing
from sklearn.preprocessing import Imputer

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
fittx=imp.fit(train)
fity=imp.fit(valid)
fitz = imp.fit(test)

train, valid, test =imp.transform(train), imp.transform(valid) , imp.transform(test)

# train, valid, test = preprocessing.scale(train), preprocessing.scale(valid), preprocessing.scale(test)





# reshape for keras LSTM
#need  [samples, time steps, features]. 
# Currently, our data is in the form: [samples, features] 
# and we are framing the problem as one time step for each sample. 
train = np.reshape(train, (train.shape[0], train.shape[1],1))
valid = np.reshape(valid, (valid.shape[0], valid.shape[1],1))
test = np.reshape(test, (test.shape[0], test.shape[1],1))

