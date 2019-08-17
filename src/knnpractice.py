# This python file is used to create the function which contains the TensorFlow session for KNN
"""
from decryptionFunctions import frequency_list_generate, IC
from collections import OrderedDict
import operator
import random
import string
from collections import Counter
from static.trigram import trigram
from cryptanalysis import *
from ALL_ENCRYPTION import *

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import tensorflow as tf

from knn import really_english_string2
from knn import score_collection


def knn_my_text_please(ciphertext):
    from knn import really_english_string2
    from knn import score_collection

    myknnydata = np.loadtxt("knnydata6.txt", dtype=int)
    myknnxdata = np.loadtxt("knnxdata6.txt", dtype=float)
    # print(myknnxdata)
    # print(len(myknnxdata))
    # print(myknnydata)
    # print(len(myknnydata))

    myknnydata3 = []
    for i in range(700):
        myknnydata3.append(0)
    for i in range(700):
        myknnydata3[i] = myknnydata[i]
    myknnydata3.append(0)

    # print(myknnydata3)
    # print(len(myknnydata3))

    myknnxdata2 = np.zeros(shape=(701, 8))
    for i in range(700):
        myknnxdata2[i] = myknnxdata[i]
    myknnxdata2[700] = score_collection(ciphertext)

    # print(myknnxdata2)
    # print(len(myknnxdata2))

    # one hot coding
    y_vals = np.eye(len(set(myknnydata3)))[myknnydata3]
    # print(y_vals)
    # print(type(y_vals))
    # print(len(y_vals))

    # normalze
    x_vals = (myknnxdata2 - myknnxdata2.min(0)) / myknnxdata2.ptp(0)
    # print(x_vals)
    # print(type(x_vals))
    # print(len(x_vals))

    np.random.seed(59)
    train_indices = np.random.choice(
        len(x_vals) - 1, round(len(x_vals) - 1), replace=False
    )
    # print(train_indices)
    # print(type(train_indices))
    # print(len(train_indices))
    # creates a list of indicies for traininf randomly and shuffled

    test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
    # print(test_indices)

    x_vals_train = x_vals[train_indices]
    x_vals_test = x_vals[test_indices]
    y_vals_train = y_vals[train_indices]
    y_vals_test = y_vals[test_indices]

    ################################# ALGORITH WRITING  ############################################

    feature_number = len(x_vals_train[0])
    # number of dimensions we are training against

    # print(feature_number)
    k = 5
    # initiation the number of nearest neigher we will be calculating the mean distance of

    x_data_train = tf.placeholder(shape=[None, feature_number], dtype=tf.float32)
    # print(x_data_train)
    # creating the x tensor with correct dimensions 4
    y_data_train = tf.placeholder(shape=[None, len(y_vals[0])], dtype=tf.float32)
    # print(y_data_train)
    # creating the y tensor with correct dimensions 3
    x_data_test = tf.placeholder(shape=[None, feature_number], dtype=tf.float32)
    # print(x_data_test)
    # testing tensor of 4 dimensions for the x data too
    # print(type(x_data_test))

    # calculate the manhattan distance
    distance = tf.reduce_sum(
        tf.abs(tf.subtract(x_data_train, tf.expand_dims(x_data_test, 1))), axis=2
    )
    # print(distance)
    # print(type(distance))
    # creates a tensor which calculates the distance

    # nearest k points
    _, top_k_indices = tf.nn.top_k(tf.negative(distance), k=k)
    top_k_label = tf.gather(y_data_train, top_k_indices)
    # print(top_k_indices)
    # a tensor storing the closest 5 indices of the data
    # print(top_k_label)
    # a tensor storing the closest 5 indices and there labels

    sum_up_predictions = tf.reduce_sum(top_k_label, axis=1)
    prediction = tf.argmax(sum_up_predictions, axis=1)
    # print(sum_up_predictions)
    # sum of 3 closest labels
    # print(prediction)
    # magnitude predicion of label of our data

    ##########################################  TRAINING PREDICTING  ##################################################

    from knn import really_english_string2
    from knn import score_collection

    # print(type(y_vals_train))
    # print(type(y_vals))
    # print(y_vals)
    # print("-------")
    # print(y_vals_train)
    # print(len(y_vals_train))

    sess = tf.Session()
    prediction_outcome = sess.run(
        prediction,
        feed_dict={
            x_data_train: x_vals_train,
            x_data_test: x_vals_test,
            y_data_train: y_vals_train,
        },
    )

    # evaluation
    accuracy = 0
    index = 0
    for pred, actual in zip(prediction_outcome, y_vals_test):
        # print("----this ya boy ------------")
        # print(pred)
        # print("---- this ya boy  ------------")
        # print(actual)
        # print(x_vals_test[index])
        index += 1
        if pred == np.argmax(actual):
            accuracy += 1

    # print(accuracy / len(prediction_outcome))
    # print(">>>>>below>>>>>>>")
    cipher_encryption_type = ""
    if pred == 0:
        cipher_encryption_type = "Ceaser"
    if pred == 1:
        cipher_encryption_type = "Vigenere"
    if pred == 2:
        cipher_encryption_type = "Columnar Transpositional"
    if pred == 3:
        cipher_encryption_type = "Beaufort"
    if pred == 4:
        cipher_encryption_type = "Beaufort"
    if pred == 5:
        cipher_encryption_type = "Porta"
    if pred == 6:
        cipher_encryption_type = "Affine"

    return cipher_encryption_type

"""
