import MovieLens
import itembasedDCF
import numpy as np
import evaluate
#userbased:1.dataMat, IDX, parDinit, disOpt
def expe_AL(nbits,para):
     trainMat, testMat=MovieLens.loadDataSet()
#     dataMat=trainMat
     dataMat=trainMat.T
     featMat=itembasedDCF.pca(dataMat,nbits)
     D,R=itembasedDCF.ITQ(featMat,nbits)
#     IDX=np.nonzero(trainMat.T)
     IDX=np.nonzero(trainMat)
     for i in range(len(para)):
#         B0,X=itembasedDCF.parDinit(trainMat.T, nbits, IDX, 5, 1, para[i], D,5)
         B0,X=itembasedDCF.parDinit(trainMat, nbits, IDX,5,1,para[i],D,5)
# B=itembasedDCF.disOpt(5,1,trainMat.T, IDX, nbits, para[i], B0, D,X,5)
         B=itembasedDCF.disOpt(5,1,trainMat, IDX, nbits, para[i], B0,D,X,5)
         ndcg=evaluate.NDCG_cal(B,D,testMat,5)
	 print ndcg
