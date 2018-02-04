# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]

z=[ 0.56721179,  0.56019029,  0.56307692,  0.56796645,  0.57447781,  0.5729688, 0.57077118]
z2=[ 0.60287093,  0.60638316,  0.61429963,  0.62008262,  0.62088591,  0.61962844, 0.61640132]
z3=[ 0.63753588,  0.64602877,  0.65044786,  0.65214559,  0.65451275,  0.65654485, 0.65793066]
z4=[ 0.63912558, 0.62861551, 0.62042475, 0.60877249, 0.58966693, 0.5712697, 0.55583806]
group_labels=[8,16,32,64,128,256,512]
#group_labels=x
plt.title('')
plt.xlabel('bits')
plt.ylabel('NDCG@5')

plt.plot(x,z,'b-^', label='ITQ')
plt.plot(x,z2,'r-+', label='ITSH')
plt.plot(x,z3,'y-x', label='UTSH')
plt.plot(x,z4,'g-D',label='binMF')

plt.xticks(x,group_labels,rotation=0)
plt.legend()
plt.show()
