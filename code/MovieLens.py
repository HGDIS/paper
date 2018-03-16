
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:12:22 2017

@author: youth
"""

import pandas as pd
import numpy as np
from scipy import sparse

def train_test(arrays, test_size=0.2):
    trainidx=[]
    testidx=[]
    for i in range(len(arrays)):
#        np.random.seed(0)
#        mask_test=np.random.rand(arrays[i]) <= test_size
        arr=np.arange(arrays[i])
        np.random.shuffle(arr)
        mask_test=arr < arrays[i]*test_size
        testidx.extend(mask_test)
        mask_train=~mask_test
        trainidx.extend(mask_train)
    return np.array(testidx), np.array(trainidx)
    
def loadDataSet(file_path, unum, vnum):
    
#从u.data中读取评分数据
    rnames=['user_id', 'movie_id', 'rating', 'timestamp']
    ratings=pd.read_table(file_path, sep='\t', header=None, 
                      names=rnames, engine='python')
#print #filtered_ratings2_new=filtered_ratings2.set_index(np.arange(999517))
    ratings["user_id"]-=1
    ratings["movie_id"]-=1

    u,v,r=ratings.user_id.values, ratings.movie_id.values, ratings.rating.values

#删除评分数少于20的用户和少于5的电影
    u_count=pd.value_counts(u)
    v_count=pd.value_counts(v)

    mask=(u_count >= unum)[u].values & (v_count >= vnum)[v].values
    u,v,r=u[mask], v[mask], r[mask]
    
#检查过滤之后的结果   
    print pd.value_counts(u), pd.value_counts(v)
    
#idx_count为处理后的用户评分数量组
    uidx_count=pd.value_counts(u)
    vidx_count=pd.value_counts(v)
    idx_split=uidx_count.sort_index().values


    idx_test, idx_train= train_test(idx_split)
    dataset=[u,v,r]
    u_train, v_train, r_train=[arr[idx_train] for arr in dataset ]
    u_test, v_test, r_test=[arr[idx_test] for arr in dataset ]

    nu=np.max(u)+1
    nv=np.max(v)+1

#构建训练集评分矩阵，测试集评分矩阵
    trainMat=sparse.coo_matrix((r_train, (u_train, v_train)), shape=(nu, nv))
    trainMat=trainMat.toarray()

    testMat=sparse.coo_matrix((r_test, (u_test, v_test)), shape=(nu, nv))
    testMat=testMat.toarray()

#去掉训练集，测试集评分矩阵中的全零行，全零列
    idx_delu=np.array([i in uidx_count.index for i in range(nu)])
    idx_delv=np.array([i in vidx_count.index for i in range(nv)])

    last_trainMat=trainMat[idx_delu]
    last_trainMat=last_trainMat[:,idx_delv]
    last_testMat=testMat[idx_delu]
    last_testMat=last_testMat[:,idx_delv] 
    return last_trainMat, last_testMat

if __name__ == '__main__':
    file_path = '/Users/eggs/youth/paper/code/data/u.data' 
    trainMat, testMat = loadDataSet(file_path, 25, 5)
    print trainMat