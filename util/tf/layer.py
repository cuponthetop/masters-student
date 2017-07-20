import tensorflow as tf


W_NAME = "w"
BiAS_NAME = "biases"


def leaky_relu(x, leak=0.2, name="leaky_relu"):
    return tf.maximum(x, leak * x, name=name)


def linear(x, output_shape, name='linear', stddev=0.02, initial_bias=0.0):
    with tf.variable_scope(name):
        weight_shape = [x.get_shape()[1], output_shape]
        w = tf.get_variable(W_NAME, weight_shape, tf.float32, tf.random_normal_initializer(stddev=stddev))
        biases = tf.get_variable(BiAS_NAME, [output_shape], initializer=tf.constant_initializer(initial_bias))

        return tf.matmul(x, w) + biases, w, biases


def deconv2d(x, output_shape, kernel_shape=[5, 5], stride_shape=[1, 2, 2, 1], stddev=0.02, initial_bias=0.0, name="deconv2d"):
    with tf.variable_scope(name):
        # filter : [height, width, output_channels, in_channels]
        filter_kernel_shape = kernel_shape + [output_shape[-1], x.get_shape()[-1]]

        w = tf.get_variable(W_NAME, filter_kernel_shape, initializer=tf.random_normal_initializer(stddev=stddev))
        biases = tf.get_variable(BiAS_NAME, [output_shape[-1]], initializer=tf.constant_initializer(initial_bias))

        deconv = tf.nn.conv2d_transpose(x, w, output_shape=output_shape, strides=stride_shape)
        deconv = tf.reshape(tf.nn.bias_add(deconv, biases), deconv.get_shape())

        return deconv, w, biases


def batch_norm(x, name="batch_norm", is_training=True, decay=0.9, epsilon=1e-5):
    return tf.contrib.layers.batch_norm(x, decay=decay, updates_collections=None,
                                        epsilon=epsilon, scale=True, is_training=is_training, scope=name)


def conv2d(x, output_shape, kernel_shape=[5, 5], stride_shape=[1, 2, 2, 1], stddev=0.02, initial_bias=0.0, name="conv2d"):
    with tf.variable_scope(name):
        filter_kernel_shape = kernel_shape + [x.get_shape()[-1], output_shape]
        w = tf.get_variable(W_NAME, filter_kernel_shape, initializer=tf.truncated_normal_initializer(stddev=stddev))
        biases = tf.get_variable(BiAS_NAME, [output_shape], initializer=tf.constant_initializer(initial_bias))

        conv = tf.nn.conv2d(x, w, strides=stride_shape, padding='SAME')
        conv = tf.reshape(tf.nn.bias_add(conv, biases), conv.get_shape())

        return conv, w, biases
