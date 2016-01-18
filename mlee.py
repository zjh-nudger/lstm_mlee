
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:39:08 2015

@author: tanfan.zjh
"""

import cPickle

import numpy
import theano


def prepare_data(seqs, labels):
    """
    Create the matrices from the datasets.
    This pad each sequence to the same lenght: the lenght of the
    longuest sequence or maxlen.
    if maxlen is set, we will cut all sequence to this maximum
    lenght.
    This swap the axis!
    """
    lengths = [len(s) for s in seqs]
    max_len = numpy.max(lengths)
    n_samples = len(seqs)
    
    x = numpy.zeros((max_len,n_samples)).astype('int64')
    x_mask = numpy.zeros((max_len,n_samples)).astype(theano.config.floatX)
    for idx,s in enumerate(seqs):
        x[:lengths[idx],idx] = s
        x_mask[:lengths[idx],idx] = 1
    ##x_mask: like x but all 1
    return x, x_mask, labels

import constant
def load_data(path='data/'+constant.dataset+'.pkl',valid_portion=0.1):
    '''
    Loads the dataset
    '''
    f=open(path,'rb')
    train_set = cPickle.load(f)
    test_set = cPickle.load(f)
    f.close()
    # split training set into validation set
    train_set_x, train_set_y = train_set
    n_samples = len(train_set_x)
    sidx = numpy.random.permutation(n_samples)#0-n_samples的随机序列，目的是打乱样本
    n_train = int(numpy.round(n_samples * (1. - valid_portion)))#训练样本个数
    valid_set_x = [train_set_x[s] for s in sidx[n_train:]]
    valid_set_y = [train_set_y[s] for s in sidx[n_train:]]
    train_set_x = [train_set_x[s] for s in sidx[:n_train]]
    train_set_y = [train_set_y[s] for s in sidx[:n_train]]
    
    return (train_set_x,train_set_y), (valid_set_x,valid_set_y), test_set
