# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:08:27 2015

@author: tanfan.zjh
"""
import constant
dataset = constant.dataset
data_dir = 'data'
prefix = '/home/liuxiaoming/tools/depvec/depvecs/'
npy = prefix + 'vecs_dep_all_50.npy'
vocab = prefix + 'vecs_dep_all_50.vocab'

train=constant.train
test=constant.test

output = data_dir+'/'+dataset+'.pkl'
emb = constant.emb

import cPickle as cp
import numpy as np

def ugly_normalize(vecs):
   normalizers = np.sqrt((vecs * vecs).sum(axis=1))
   normalizers[normalizers==0]=1
   return (vecs.T / normalizers).T

class Embeddings:
   def __init__(self, vecsfile, vocabfile=None, normalize=True):
      if vocabfile is None: vocabfile = vecsfile.replace("npy","vocab")
      self._vecs = np.load(vecsfile)
      self._vocab = file(vocabfile).read().split()
      if normalize:
         self._vecs = ugly_normalize(self._vecs)
      self._w2v = {w.lower():i for i,w in enumerate(self._vocab)}

   @classmethod
   def load(cls, vecsfile, vocabfile=None):
      return Embeddings(vecsfile, vocabfile)

   def word2vec(self, w):
      return self._vecs[self._w2v[w]]

print 'process start..'
embedding=Embeddings.load(vecsfile=npy,vocabfile=vocab)

dict_mlee={}

train_file = open(train,'r')
test_file = open(test,'r')

train_labels=[]
train_data=[]
index=0
for train_line in train_file:
    items = train_line.split()
    train_labels.append(int(items[0]))
    data_line = []
    for item in items[1:]:
        if item == 'NULL':
            #data_line.append(0)
            continue
        if dict_mlee.has_key(item.lower()):
            data_line.append(dict_mlee[item.lower()])
        else:
            dict_mlee[item.lower()] = index
            data_line.append(index)
            index += 1
    train_data.append(data_line)
train_file.close()

test_labels=[]
test_data=[]
for test_line in test_file:
    items = test_line.split()
    test_labels.append(int(items[0]))
    data_line = []
    for item in items[1:]:
        if item == 'NULL':
            #data_line.append(0)
            continue
        if dict_mlee.has_key(item.lower()):
            data_line.append(dict_mlee[item.lower()])
        else:
            pass
            #data_line.append(0)
    test_data.append(data_line)
test_file.close()

f = open(output, 'wb')
cp.dump((train_data, train_labels), f, -1)
cp.dump((test_data, test_labels), f, -1)
f.close()

word_vecs = []
rand_vec = np.random.uniform(-0.25,0.25,200)
#word_vecs.append(rand_vec)
from collections import OrderedDict
dict_mlee_rev = {i:w for w,i in dict_mlee.iteritems()}
dict_mlee_rev_order = OrderedDict(dict_mlee_rev)

emb_vocab = {w.lower() for w in embedding._vocab}
for _,v in dict_mlee_rev_order.iteritems():
    if v in emb_vocab:
        word_vecs.append(embedding.word2vec(v))
    else:
        word_vecs.append(rand_vec)

print np.shape(np.asarray(word_vecs))#4324
#print len(dict_mlee_rev_order)#4323

f_emb = open(emb,'wb')
cp.dump(np.asarray(word_vecs),f_emb,-1)
f_emb.close()

print 'done..'