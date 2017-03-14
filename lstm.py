# source activate py35


from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam, SGD
# get cleaned training data from clean.py
from clean import train, train_label
# from clean import valid, valid_label
import matplotlib.pyplot as plt


num_features=train.shape[1]

model = Sequential()
model.add(LSTM(200,input_shape=[num_features,1]))
# model.add(LSTM(16,input_dim=1))

model.add(Dense(2))
model.add(Activation('softmax'))
op=SGD()
model.compile(	loss='categorical_crossentropy',
				optimizer=op,
				metrics=["accuracy"]
				)


h=model.fit(train,
			train_label,
			batch_size=100,
			nb_epoch=10,
			validation_split=.2,
			verbose=1)

# model.predict_classes(train)

# plot accuracy over training epochs
plt.plot(h.history['acc'])
plt.plot(h.history['val_acc'])
plt.title('accuracy of training and validation data')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')

plt.show()