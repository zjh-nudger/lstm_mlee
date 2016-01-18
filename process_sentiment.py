# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:54:14 2015

@author: tanfan.zjh
"""

train = 'yelp_academic_dataset_review_Las Vegas_train.txt'
test = 'yelp_academic_dataset_review_Las Vegas_test.txt'

train_file = open(train,'r')
test_file = open(test,'r')

word_dict = {}

train_label = []
train_data = []
index = 0
for line in train_file:
    tup = line.split('=')
    train_label.append(int(tup[0][0]))
    toks = tup[1].split()
    data_line = []
    for word in toks:
        if word not in word_dict:
            word_dict[index] = word
            data_line.append(index)
            index += 1
        else:
            data_line.append(word_dict[word])
    train_data.append(data_line)
train_file.close()

test_data = []
test_label = []
for line in test_file:
    tup = line.split('=')
    test_label.append(int(tup[0][0]))
    toks = tup[1].split()
    data_line = []
    for word in toks:
        if word not in word_dict:
            continue
        else:
            data_line.append(word_dict[word])
    test_data.append(data_line)
test_file.close()

import cPickle as cp
output = 'sentiment_bao.pkl'
f = open(output, 'wb')
cp.dump((train_data, train_label), f, -1)
cp.dump((test_data, test_label), f, -1)
f.close()