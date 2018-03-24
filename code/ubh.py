import MovieLens
import itembasedDCF

def ubh(alpha, nbits, k):
    if k==5:
        unum=25
	vnum=5
    else:
	unum=50
	vnum=10

    trainMat, testMat=MovieLens.loadDataSet(unum,vnum)
    featMat=itembasedDCF.pca(trainMat,nbits)
    B,R=itembasedDCF.ITQ(featMat,nbits)
    IDX=nonzero(trainMat.T)
    D0,X=itembasedDCF.parDinit(trainMat.T,nbits,IDX,5,1,alpha,B,5)
    D=itembasedDCF.disOpt(5,1,trainMat.T,IDX,nbits,alpha,B,D0,X,10)
    return B,D,testMat
