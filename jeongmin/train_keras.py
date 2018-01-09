from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense
from keras import initializers, optimizers
import keras.backend.tensorflow_backend as K
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Process the datasets
with open('./jeongmin/processed_data.txt', 'rb') as f:
    tmp = pickle.load(f)
    X_train = tmp['x']
    Y_train = tmp['y']

X_train = np.array(X_train, dtype=np.float32)
Y_train = np.array(Y_train, dtype=np.float32)

X_val = X_train[1000:]
Y_val = Y_train[1000:]
X_train = X_train[:1000]
Y_train = Y_train[:1000]

# Define accuracy function
def custom_accuracy(y_true, y_pred):
    return 1 - K.abs(y_true[0] - y_pred[0])

# Define callback function for earlystopping
early_stopping = EarlyStopping(patience=10)

# Design the model
model1 = Sequential() # xavier normal initialization
model1.add(Dense(11, input_dim=11, kernel_initializer='glorot_normal', bias_initializer=initializers.random_normal(),
                 activation='relu'))
model1.add(Dense(11, kernel_initializer='glorot_normal', bias_initializer=initializers.random_normal(),
                 activation='relu'))
model1.add(Dense(1, kernel_initializer='glorot_normal', bias_initializer=initializers.random_normal()))

model1.compile(optimizer=optimizers.adam(), loss='mean_absolute_error', metrics=[custom_accuracy])

hist = model1.fit(X_train, Y_train, epochs=500, batch_size=10, validation_data=(X_val, Y_val), callbacks=[early_stopping])

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['custom_accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_custom_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
