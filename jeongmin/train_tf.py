import tensorflow as tf
import pickle
import numpy as np

with open('./processed_data.txt', 'rb') as f:
    tmp = pickle.load(f)
    x_data = tmp["x"]
    y_data = tmp["y"]
        
tf.set_random_seed(777)
print(x_data.__len__())

learning_rate = 0.0001

x_data = np.array(x_data, dtype=np.float32)
y_data = np.array(y_data, dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 11])
Y = tf.placeholder(tf.float32, [None, 1])

# first layer (input): 13 -> 11
W1 = tf.get_variable("W1", shape=[11, 11],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([11]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

# second layer (hidden): 11 -> 11
W2 = tf.get_variable("W2", shape=[11, 11],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([11]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

# third layer (output): 11 -> 1
W3 = tf.get_variable("W3", shape=[11, 1],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([1]))
hypothesis = tf.matmul(L2, W3) + b3

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
error = tf.abs(tf.subtract(y_data, hypothesis))
accuracy = 1 - tf.reduce_mean(tf.cast(error, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(20000):
        sess.run([optimizer, cost], feed_dict={X: x_data, Y: y_data})
        if i % 100 == 0:
            print(i, sess.run(cost, feed_dict={
                  X: x_data, Y: y_data}), sess.run([W1, W2]))

        h, a = sess.run([hypothesis, accuracy], feed_dict={X: x_data, Y: y_data})
        print("\nHypothesis: ", h, "\nCorrect: ", y_data, "\nAccuracy: ", a)
        # print(i, "Accuracy: ", a)
        # if i % 100 == 0: print(i)
