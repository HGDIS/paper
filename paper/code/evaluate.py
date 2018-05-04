<<<<<<< HEAD:evaluate.py
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:21:10 2017

@author: youth
"""

import numpy as np
import math
import pandas as pd

def haming_distance(s1,s2):
    s1=np.array(s1)
    s2=np.array(s2)
    assert len(s1)==len(s2)
    ham_dist=[sum(ch1!=ch2 for ch1, ch2 in zip(s1, s2))]
    return ham_dist
    
def dot_distance(s1,s2):
    dot_dist=np.dot(s1.T,s2)[0][0]
    return dot_dist
    
def NDCG_cal(U, V, testMat,k):
    m,n=np.shape(U)
    NDCG=0.0
    for i in range(n):
        testi=np.nonzero(testMat[i])
        rate=[testMat[i][t] for t in testi[0]]
        ratei=sorted(rate, reverse=True)[:k]
#计算IDCG
        IDCG=0.0
        for s in range(len(ratei)):
            IDCG+=float((math.pow(2, ratei[s])-1))/float((math.log(s+2, 2)))
#计算DCG            
        disti=[]
        for j in range(len(testi[0])):
            dist=dot_distance(U[:,i], V[:,testi[0][j]])
            disti.extend(dist)
        s=pd.Series(disti, index=testi[0])
        s.sort()
        recomrate=[testMat[i][z] for z in s.index[:k]]
        DCG=0.0
        for x in range(len(recomrate)):
            DCG+=(math.pow(2, recomrate[x])-1)/(math.log(x+2, 2))
        NDCG=NDCG+ DCG/IDCG
    return NDCG/n
        
            
            
        
    
    
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:21:10 2017

@author: youth
"""

import numpy as np
import math
import pandas as pd

def haming_distance(s1,s2):
    s1=np.array(s1)
    s2=np.array(s2)
    assert len(s1)==len(s2)
    ham_dist=[sum(ch1!=ch2 for ch1, ch2 in zip(s1, s2))]
    return ham_dist
    
def dot_distance(s1,s2):
    s1=np.array(s1)
    s2=np.array(s2)
    dot_dist=np.dot(s1,s2)
    return dot_dist
    
def NDCG_cal(U, V, testMat,k,dist_method):
    m,n=np.shape(U)
    NDCG=0.0
    for i in range(n):
        testi=np.nonzero(testMat[i])
        rate=[testMat[i][t] for t in testi[0]]
        ratei=sorted(rate, reverse=True)[:k]
#计算IDCG
        IDCG=0.0
        for s in range(len(ratei)):
            IDCG+=float((math.pow(2, ratei[s])-1))/float((math.log(s+2, 2)))
#计算DCG            
        disti=[]
        for j in range(len(testi[0])):
            dist=dist_method(U[:,i], V[:,testi[0][j]])
            disti.extend(dist)
        s=pd.Series(disti, index=testi[0])
        s.sort()
        recomrate=[testMat[i][z] for z in s.index[:k]]
        DCG=0.0
        for x in range(len(recomrate)):
            DCG+=(math.pow(2, recomrate[x])-1)/(math.log(x+2, 2))
        NDCG=NDCG+ DCG/IDCG
    return NDCG/n
        
            
            
        
    
    
>>>>>>> 3031c5efe54634cadb3daa3372663aafa220d7e0:code/evaluate.py
