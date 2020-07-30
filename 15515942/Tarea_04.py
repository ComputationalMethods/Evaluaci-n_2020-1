#!/usr/bin/env python3


import numpy as np
from scipy import optimize 
import scipy as sp


def function(x):
    return sp.sqrt(x**2+1)+np.exp(x)*sp.sin(x)-7



if __name__=='__main__':

    print("\n\n")
    print( __name__)
    
    a = 0.0
    b = 2.0


    result,r=optimize.bisect(function,a,b,full_output=True)
    print(result)
