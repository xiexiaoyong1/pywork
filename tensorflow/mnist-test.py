#!/usr/bin/python
#！coding:utf-8
import input_data
mnist = input_data.read_data_sets("./MNIST_data/train/", one_hot=True)

import tensorflow as tf
