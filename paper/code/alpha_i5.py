#itembased,NDCG@5,nbits=256 
#alpha[0.0001,0.001,0.01,0.1,1,10,100]

import MovieLens
import itembasedDCF
import evaluate
import numpy as np

para=[8,16,32,64,128,256,512]
NDCG5=[]
for i in range(5):
    print "the",i,"time"
    trainMat, testMat=MovieLens.loadDataSet(25, 5)
    PARA=[]
    for j in range(len(para)):
        featMat=itembasedDCF.pca(trainMat.T, para[j])
        D,R=itembasedDCF.ITQ(featMat,para[j])
        IDX=np.nonzero(trainMat)
        B0,X=itembasedDCF.parDinit(trainMat,para[j],IDX,5,1,10,D,5)
        B=itembasedDCF.disOpt(5,1,trainMat,IDX, para[j],10, B0,D,X,10)
        ndcg=evaluate.NDCG_cal(B,D,testMat,5)
	PARA.append(ndcg)
    print PARA
    NDCG5.append(PARA)
result=np.mean(NDCG5,axis=0)
print NDCG5,result
