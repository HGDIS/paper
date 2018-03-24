import MovieLens
import itembasedDCF
import evaluate
import numpy as np

para=[8,16,32,64,128,256,512]
NDCG10=[]
for i in range(5):
    print 'the', i, 'time'
    trainMat,testMat=MovieLens.loadDataSet(50,5)
    PARA=[]
    for j in range(len(para)):
        featMat=itembasedDCF.pca(trainMat,para[j])
	B,R=itembasedDCF.ITQ(featMat,para[j])
	IDX=np.nonzero(trainMat.T)
	D0,X=itembasedDCF.parDinit(trainMat.T,para[j],IDX,5,1,10,B,5)
	D=itembasedDCF.disOpt(5,1,trainMat.T,IDX,para[j],10,D0,B,X,10)
	ndcg=evaluate.NDCG_cal(B,D,testMat,10)
	PARA.append(ndcg)
    print PARA
    NDCG10.append(PARA)
result=np.mean(NDCG10,axis=0)
print NDCG10,result
