# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:43:36 2015

@author: tanfan.zjh
"""
import theano

class Tree:
    def __init__(self,idx_array,parent_array):
        
        pass
    
idx = theano.tensor.vector('idx',dtype='int32')
parent = theano.tensor.vector('parent',dtype='int32')
print dir(idx)
## idx [1,2,3,4,5,6]
## par [0,1,1,2,2,3]
def output(idx,parent):
    
    return [idx[1],parent.ptp()]


f = theano.function(inputs=[idx,parent],outputs=output(idx,parent))

import numpy
i = [1,2,3,4,5,6]
i = numpy.asarray(i)
p = [0,1,1,2,2,3]
n = [1,2,2,3,3,3]
p = numpy.asarray(p)
print f(i,p)
