import tensorflow as tf
import numpy as np
from MachineLearning.MNIST import model
from MachineLearning.MNIST import input_data
import matplotlib.pyplot as plt


def show_image(mnist_image):
    image = np.reshape(mnist_image, newshape=[28, -1])
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()


mnist = input_data.read_data_sets('data', one_hot=True)

input_data = tf.placeholder(tf.float32, [None, 784])
keep_prob = tf.placeholder(tf.float32)
forward_result = model.forward(input_data, keep_prob)
predict_result = tf.argmax(forward_result, 1)
saver = tf.train.Saver()
index = 991  # 测试集图片索引
with tf.Session() as sess:
    image = mnist.test.images[index]
    show_image(image)

    sess.run(tf.global_variables_initializer())
    saver.restore(sess, "save_model/model.ckpt")
    _predict_result = sess.run([predict_result], feed_dict={input_data: [image], keep_prob: 1.0})

    _correct_result = np.argmax(mnist.test.labels[index])

    print('predict={} ,correct={}'.format(_predict_result[0][0], _correct_result))