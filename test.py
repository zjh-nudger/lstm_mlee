# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:43:36 2015

@author: tanfan.zjh
"""
'''
import cPickle
f=open('imdb.pkl','rb')
train = cPickle.load(f)
test = cPickle.load(f)
f.close()
print len(train[0])
print len(train[1])
print train[0][:1]

import numpy
print numpy.random.permutation(6)

seq=[[1,2,3,4,5,6,7],[1],[1,2,3,4,5],[1,2],[1,2,3,4,5,6],[1,2,3],[1,2,3,4]]
print sorted(range(len(seq)), key=lambda x: len(seq[x]))

import numpy
print numpy.random.rand(1,2)

'''
'''
import sys
print >> sys.stderr
'''
'''
import numpy
def ortho_weight(ndim):
    W = numpy.random.randn(ndim, ndim)
    u, s, v = numpy.linalg.svd(W)
    return u
#print ortho_weight(2)
n=6
r = numpy.concatenate([ortho_weight(n),ortho_weight(n),ortho_weight(n),ortho_weight(n)],
                       axis=1)
print numpy.shape(r)
'''
'''
import numpy
import cPickle as cp
#print numpy.mod(2000,100)
f = open('imdb.pkl','rb')
c1 = cp.load(f)
c2 = cp.load(f)
print c1[1][0]
'''
dic = {1:'a',3:'c',2:'b'}
from collections import OrderedDict
od = OrderedDict(dic)
for w,i in od.iteritems():
    print w,i