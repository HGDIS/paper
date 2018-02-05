import MovieLens
import itembasedDCF
import evaluate
import numpy as np
NDCG=[]
Bit=[8,16,32,64,128,256,512]
for i in range(5):
    print 'the', i, 'time'
    nbit=[]
    for j in range(len(Bit)):
        trainMat, testMat=MovieLens.loadDataSet(50,5)
        featu=itembasedDCF.pca(trainMat,Bit[j])
        feati=itembasedDCF.pca(trainMat.T,Bit[j])
        B,Ru=itembasedDCF.ITQ(featu,Bit[j])
        D,Ri=itembasedDCF.ITQ(feati,Bit[j])
        ndcg=evaluate.NDCG_cal(B,D,testMat,10)
        nbit.append(ndcg)
    print NDCG
    NDCG.append(nbit)
result=np.mean(NDCG,axis=0)
print result
