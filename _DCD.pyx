import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "DCD.h":
    void DCD(double *b, double *MM, double *Ms, double *x, int maxItr, int r)

def DCD_func(np.ndarray[double, ndim=1,mode="c"] b not None, np.ndarray[double, ndim=1, mode="c"] MM not None, np.ndarray[double, ndim=1, mode="c"] Ms not None, np.ndarray[double, ndim=1,mode="c"] x not None, int maxItr, int r):
    DCD(<double*> np.PyArray_DATA(b), <double*> np.PyArray_DATA(MM),<double*> np.PyArray_DATA(Ms), <double*> np.PyArray_DATA(x), maxItr,  r)
