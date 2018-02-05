import MovieLens
import mf_als
import numpy as np
import evaluate

trainMat,testMat=MovieLens.loadDataSet(25,5)
trainMat=np.mat(trainMat)
nbits=[8,16,32,64,128,256,512]
NDCG =[]
for i in range(len(nbits)):
    X,Y= mf_als.mf_als(trainMat,nbits[i],20,0.1)
    X=mf_als.sgn(X)
    Y=mf_als.sgn(Y)
    ndcg=evaluate.NDCG_cal(X,Y,testMat,5)
    print i,ndcg
    NDCG.append(ndcg)
print NDCG
