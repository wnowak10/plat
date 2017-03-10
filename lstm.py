# source activate py35


from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam
# get cleaned training data from clean.py
from clean import train, train_label
from clean import valid, valid_label
import matplotlib.pyplot as plt


# print(train_label.shape)
num_features=3

model = Sequential()
model.add(LSTM(1,input_shape=[num_features,1]))
# model.add(LSTM(16,input_dim=1))

model.add(Dense(2))
model.add(Activation('softmax'))
adam=Adam()
model.compile(	loss='categorical_crossentropy',
				optimizer=adam)


h=model.fit(train,
			train_label,
			batch_size=100,
			nb_epoch=10,
			verbose=1)

model.predict_classes(train)

# plt.plot(h['acc'])
# plt.show()