import tensorflow as tf

def get_weights(shape):
    w_variable = tf.get_variable("w_variable", shape=shape, trainable=True)
    return w_variable

    # initial = tf.truncated_normal(shape,stddev=0.1)
    # return tf.Variable(initial)


def get_bias(shape):
    b_variable = tf.get_variable("b_variable", shape=shape, trainable=True)
    return b_variable


def conv2d_relu(input, filter, bias):
    features = tf.nn.conv2d(input=input,
                            filter=filter,
                            strides=[1, 1, 1, 1],
                            padding='SAME')
    return tf.nn.relu(features=(features + bias))


def max_pool(input):
    return tf.nn.max_pool(value=input,
                          ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1],
                          padding='SAME')


def forward(input_data, keep_prob):
    input_data = tf.reshape(input_data, [-1, 28, 28, 1])
    with tf.variable_scope("layer_1"):
        w1 = get_weights([5, 5, 1, 32])
        b1 = get_bias([32])
        conv1 = conv2d_relu(input_data, w1, b1)
        pool1 = max_pool(conv1)

    with tf.variable_scope("layer_2"):
        w2 = get_weights([5, 5, 32, 64])
        b2 = get_bias([64])
        conv2 = conv2d_relu(pool1, w2, b2)
        pool2 = max_pool(conv2)

    with tf.variable_scope("full_connection_1"):
        pool2_flat = tf.reshape(pool2, shape=[-1, 7 * 7 * 64])
        w3 = get_weights([7 * 7 * 64, 1024])
        b3 = get_bias([1024])
        fc1 = tf.nn.relu(tf.matmul(pool2_flat, w3) + b3)
        fc1_drop = tf.nn.dropout(fc1, keep_prob)

    with tf.variable_scope("full_connection_2"):
        w4 = get_weights([1024, 10])
        b4 = get_bias([10])
        fc2 = tf.matmul(fc1_drop, w4) + b4
        softmax = tf.nn.softmax(fc2)
    return softmax
