import MovieLens
import itembasedDCF
import evaluate
import numpy as np

#para=[8,16,32,64,128,256,512]
alpha = [0.0001,0.001,0.01,0.1,1,10,100]
NDCG5=[]
for i in range(5):
    print 'the',i,'time'
    trainMat,testMat=MovieLens.loadDataSet(25,5)
    PARA=[]
    for j in range(len(alpha)):
       # featMat=itembasedDCF.pca(trainMat,para[j])
	featMat = itembasedDCF.pca(trainMat, 256)
	B,R=itembasedDCF.ITQ(featMat,256)
	IDX=np.nonzero(trainMat.T)
	D0,X=itembasedDCF.parDinit(trainMat.T,256,IDX,5,1,10,B,5)
	D=itembasedDCF.disOpt(5,1,trainMat.T,IDX,256,alpha[j],D0,B,X,10)
	ndcg=evaluate.NDCG_cal(B,D,testMat,5)
	PARA.append(ndcg)
    print PARA
    NDCG5.append(PARA)
result=np.mean(NDCG5,axis=0)
print NDCG5,result
