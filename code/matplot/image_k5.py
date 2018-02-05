<<<<<<< HEAD:matplot/image_k5.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x=[0,1,2,3,4,5,6]

z=[ 0.56721179,  0.56019029,  0.56307692,  0.56796645,  0.57447781,  0.5729688, 0.57077118]
z2=[ 0.60287093,  0.60638316,  0.61429963,  0.62008262,  0.62088591,  0.61962844, 0.61640132]
z3=[ 0.63753588,  0.64602877,  0.65044786,  0.65214559,  0.65451275,  0.65654485, 0.65793066]
#z4=[ 0.63617806,0.62763517,0.62405642,0.61015035,0.59176032,0.57158875,0.55873138]
Z4 = [ 0.63912558, 0.62861551, 0.62042475, 0.60877249, 0.58966693, 0.5712697, 0.55583806]
z5=[ 0.45275835,  0.46080956,  0.46916936,  0.51002914,  0.55379194,0.57093167,  0.57010315]
group_labels=[8,16,32,64,128,256,512]
#group_labels=x
plt.title('')
plt.xlabel('bits')
plt.ylabel('NDCG@5')

plt.plot(x,z,'b-^', label='ITQ')
plt.plot(x,z2,'r-+', label='ITSH')
plt.plot(x,z3,'y-x', label='TSH')
plt.plot(x,z4,'g-D',label='binMF')
#plt.plot(x,z5,'r-D', label = 'MF_ALS')

plt.xticks(x,group_labels,rotation=0)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1),ncol=2,shadow=False)
plt.show()
=======
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
>>>>>>> 85d42eb5e021611d984a0cf78d54407d42a81e7f:code/matplot/image_k5.py
