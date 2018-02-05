#include <string.h>
#include <math.h>
void DCD(double *b, double *MM, double *Ms, double *x, int maxItr, int r) {
    int i,k,it,no_change_count;
    double ss;
    int converge = 0; 
    it = 0;
    while (converge==0){
	no_change_count = 0;
	for (k = 0; k < r; k ++){
	    ss = 0;
	    for (i = 0; i < r; i ++){
	        if (i != k)
			ss += MM[k+i*r]*b[i];}
	    ss -= Ms[k]+x[k];
	    if (ss > 0){
		if (b[k] == -1)
		    no_change_count ++; 
		else
	            b[k] = -1;
		 }
	    else if (ss < 0){
		if (b[k] == 1)
		    no_change_count ++;
		else
		    b[k] = 1;
	         }
	    else
		no_change_count ++;
	}
        if ((it >= (int)maxItr-1) || (no_change_count == r))
	    converge = 1;
	it ++;
}
}
