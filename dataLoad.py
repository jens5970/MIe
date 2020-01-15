import numpy as np
from io import StringIO # StringIO behaves like a file object

def dataLoad(filename):
    # DATALOAD takes a text-string as input and returns a matrix.
    # The function makes the text-string to an matrix,
    # removes the lines which have errors
    # and removes those lines from the matrix
    # Author: Jens Beck, S183829
    ############################
    ### Convert txt to matrix:
    filein = open(filename, "r") # Opens the file for reading
    lines = filein.readlines() # Reads all lines into an array
    smalltxt = "".join(lines) # Joins the lines into one big string
    c = StringIO(smalltxt) 
    M = np.loadtxt(c) # M = The matrix
    
    ############################
    ### Remove invalid lines and give error-message:
    Ar = np.size(M[:,0]) #Number of rows
    vErr = np.array([], dtype=int) #Array to remeber lines with errors
    
    # Determine which lines have an error, and priting of error-message:
    for i in range(Ar):
        if (M[i,0] <= 10):
            vErr = np.concatenate((vErr,np.array([i])))
            print("Error in line {:.0f}. The temperature is to low. The temperature has to be between 10 and 60.".format(i + 1))
        elif (M[i,0] >= 60):
            vErr = np.concatenate((vErr,np.array([i])))
            print("Error in line {:.0f}. The temperature is to high. The temperature has to be between 10 and 60.".format(i + 1))
        elif (M[i,1] <= 0):
            vErr = np.concatenate((vErr,np.array([i])))
            print("Error in line {:.0f}. The Growth rate is not a positive number. The Growth rate has to be a positive number.".format(i + 1))
        elif ((M[i,2] < 1) or (M[i,2] > 4)):
            vErr = np.concatenate((vErr,np.array([i])))
            print("Error in line {:.0f}. Bacteria has to be 1, 2, 3 or 4 which it is not.".format(i + 1))
    N = np.delete(M, vErr, 0) # Delete error-lines from matrix
    
    return N













