# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:17:33 2017

@author: youth
"""

import numpy as np
import evaluate

def mf_als(R,K, steps, beta):
    M, N = R.shape
    X = np.random.rand(M, K)
    X = np.mat(X)
    Y = np.random.rand(N, K)
    Y = np.mat(Y)
    I = np.mat(np.eye(K))

    err = []
    it = []
    for step in xrange(steps):

        X1 = []
        Y1 = []

        P = (Y.T * Y + beta * I).I * Y.T

        for i in xrange(M):
            X1.append([j[0, 0] for j in (P * R[i, :].T)])
        X = np.mat(X1)

        Q = (X.T * X + beta * I).I * X.T
        for i in xrange(N):
            Y1.append([j[0, 0] for j in (Q * R[:, i])])
        Y = np.mat(Y1)

#        it.append(step)
#       err.append(numpy.sqrt(numpy.sum(pow(numpy.array(R - X * Y.T), 2)) / (M * N)))

    return X,Y


def sgn(dataMat):
    m,n=np.shape(dataMat)
    dataMean=np.median(dataMat,axis=1)
    for i in range(m):
        meanData=dataMat[i]-dataMean[i]
	for j in range(n):
	    if meanData[0,j]>=0:
	        dataMat[i,j]=1
	    else:
	        dataMat[i,j]=-1
    return dataMat.T
