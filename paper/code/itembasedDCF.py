from compiler.ast import flatten
import DCD
from numpy import *
import numpy as np
from scipy import sparse
from scipy import linalg
import copy

#apply pca to get low dimensial feature vect of item
def pca(dataMat,nbits):
    meansVals=np.mean(dataMat,axis=0)         
    meanRemoved=dataMat-meansVals
    covMat=np.cov(meanRemoved,rowvar=0)         
    eigVals,eigVects=linalg.eig(np.mat(covMat))
    eigVects=eigVects.real
    eigValInd=np.argsort(eigVals)
    eigValInd=eigValInd[:-(nbits+1):-1]
    redEigVects=eigVects[:,eigValInd]
    lowDataMat=np.dot(meanRemoved,redEigVects)
    return lowDataMat
 
#sgn:if i>0,i=1,else i=-1
def sgn(dataMat):
    m,n=np.shape(dataMat)
    for i in range(m):
 		  for j in range(n):
 			   if dataMat[i,j]>=0:
 			       dataMat[i,j]=1.0
 			   else:
 			       dataMat[i,j]=-1.0
    return dataMat
 
#apply ITQ to get item binary codes
def ITQ(feaMat,nbits): 
    rotMat=np.random.rand(nbits,nbits)
    rotMat=np.mat(rotMat)
    U,Sigma,VT=linalg.svd(rotMat)
    R=U[:,0:nbits]
    for i in range(51):
        UX=np.dot(feaMat,R)
        UX=sgn(UX)
        C=np.dot(UX.T,feaMat)
        UB,Sigma1,UA=linalg.svd(C)
        UB=UB.T
        R=np.dot(UA.T,UB)
    return UX.T,R
 
def normalize(v):
    norm=linalg.norm(v)
    if norm==0:
 	     return v
    return v/norm
 
def myMGS(U,K): #K:nbits
    m,n=np.shape(U)
    U=np.column_stack((U,np.mat(np.zeros([m,K-n]))))
    for i in range(n,K):
     		v=np.mat(np.random.rand(m,1))
        v=v-np.mean(v)
 		for j in range(i+1):
 			v=v-float(U[:,j].T*v)*U[:,j]
 		v=normalize(v)
 		U[:,i]=v
 	return U
 
 
def upDateSVD(W):
     b,n=shape(W)
     m=mean(W,1)
     JW=W-m
     JW=JW.T
     eigval,P=linalg.eig(JW.T*JW)
     eigval=eigval.real
     P=P.real
     indval=argsort(eigval)
     lowval=indval[0]
     if eigval[lowval]>1e-10:
         H_v=sqrt(n)*P*(JW*P*diag(1./sqrt(eigval))).T
     else:
         zeroidx=(eigval >1e-10)
         Q=JW*P[:,zeroidx]*diag(1./sqrt(eigval[zeroidx]))
         Q=myMGS(Q,b)
         H_v=sqrt(n)*P*Q.T
     return H_v
 
def scaleScore(s,scale,maxS,minS):
     s=(s-minS)/(maxS-minS)
     s=2*scale*s-scale
     return s
     
 #initialize B,X    
def parDinit(S,nbits,IDX,maxS,minS,alpha,D,maxItr):#IDX=nonzero(S)
     m,n=shape(S)
     B=mat(random.rand(nbits,m))
     X=upDateSVD(B)
     it=1
     tol=1e-6
     converge=False
     while(converge==False):
        print "the",it,"times iteration"
        B0=copy.copy(B)
        X0=X
        for i in range(m):
            IDXi=IDX[1][IDX[0]==i]
            Di=D[:,IDXi]
            Si=S[i,IDXi]
            if(len(Si)==0):
                 continue
            else:
                 Si=scaleScore(Si,nbits,maxS,minS)
                 Q=dot(Di,Di.T)+alpha*len(Si)*eye(nbits)
                 L=dot(Di,mat(Si).T)+2*alpha*X[:,i]
		 Qi=linalg.inv(Q)
                 B[:,i]=Qi*L
        X=upDateSVD(B)
        if(it>=maxItr or max([linalg.norm(B-B0,'fro'),linalg.norm(X-X0,'fro')])<m*tol):
             converge=True
        else:
             it+=1
     return B,X 
#iterate to optimize user's binary codes
def disOpt(maxS, minS, S, IDX, nbits, alpha, B, D, X,maxItr2):
    converge=False
    it=1
    usernum=S.shape[0]
    while(converge==False):
        print "the", it, "th times iteration"
        B1=copy.copy(B)
	for i in range(usernum):
	    IDXi=IDX[1][IDX[0]==i]
	    #d: items rated by the ith user
	    d=mat(D[:,IDXi])
	    #Si: ratings of items rated by the ith user
	    Si=mat(S[i,IDXi])
	    #b: binary codes of the ith user
	    b=B[:,i].flatten().getA()[0]
	    #update the binary codes of the ith user
	    # bi=parDopt(b,dot(d,d.T),d*scaleScore(Si.T,nbits,maxS,minS), alpha*X[:,i],maxItr2,nbits)
	    MM=dot(d,d.T).flatten().getA()[0]
	    Ms=d*scaleScore(Si.T, nbits, maxS, minS)
	    Ms=Ms.flatten().getA()[0]
	    Xi=alpha*X[:,i].flatten().getA()[0]
	    DCD.DCD_func(b, MM, Ms, Xi, maxItr2, nbits)
	    B[:,i]=mat(b).reshape(nbits,1)
	X=upDateSVD(B)
	if it >= maxItr2 or sum(B!=B1)==0:
	    converge=True
	else:
	    it+=1
    return B
