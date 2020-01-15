import numpy as np
import math
import pandas as pd

def filterData(M,filterBac,filterLBound,filterUBound):
    # Input: M = matrix with data, filterBac = which bacteria there should be filtered
    #           filterLBound = lower bound for filter, filterUBound = upper bound for filter.
    # Ouput: N = matrix with the data, which has been correted according to the filter.
    #
    # Author: Jens Beck, S183829
    ##############################
    filterBac = filterBac.lower() # makes the letters lowercase
    vBac = np.array(["salmonella enterica","bacillus cereus","listeria","brochothrix thermosphacta"])
    for i in range(4): # Finds the number for the bacteria
        if filterBac == vBac[i]:
            filterBacN = i + 1
    Ar = np.size(M[:,0]) #Number of rows
    vRem = np.array([], dtype=int) #Array to remeber lines there should be deleted
    
    # Determine which lines there should be removed
    for i in range(Ar):
        if (M[i,2] == filterBacN):
            if ((M[i,1] < filterLBound) or (M[i,1] > filterUBound)):
                vRem = np.concatenate((vRem,np.array([i])))
    N = np.delete(M, vRem, 0) # Delete lines from matrix
    return N











