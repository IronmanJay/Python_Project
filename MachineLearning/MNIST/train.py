import tensorflow as tf
from MachineLearning.MNIST import model
from MachineLearning.MNIST import input_data


def get_loss(input_lables, perdict_lables):
    cross_entropy = -tf.reduce_sum(input_lables * tf.log(perdict_lables))
    return cross_entropy


# prepare mnist data
mnist = input_data.read_data_sets('data', one_hot=True)

# super params
learning_rate = 1e-4

# placeholder
input_data = tf.placeholder(tf.float32, [None, 784])
input_labels = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

forward_result = model.forward(input_data, keep_prob)

loss = get_loss(input_labels, forward_result)

correct_prediction = tf.equal(tf.argmax(forward_result, 1), tf.argmax(input_labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# backward
train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# save model
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch_data, batch_labels = mnist.train.next_batch(10)
        _loss, _train_step, _accuracy = sess.run([loss, train_step, accuracy],
                                                 feed_dict={input_data: batch_data, input_labels: batch_labels,
                                                            keep_prob: 0.5})
        print('step = {}, loss = {}, accuracy= {:.2f}'.format(i, _loss, _accuracy))

    saver.save(sess, 'save_model/model.ckpt')
    summary_writer = tf.summary.FileWriter('./logs/', sess.graph)
    print('test accuracy {:.4f}'.format(
        accuracy.eval(feed_dict={input_data: mnist.test.images, input_labels: mnist.test.labels, keep_prob: 1})))
