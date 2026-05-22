import numpy as np 

def max_abs_sum(A) : 
    # Example i=3 , j=3 : max( |a11|+|a21|+|a31| , |a12|+|a22|+|a32| , |a13|+|a23|+|a33| )
    # which means max of absolute sum of each column 
    
    # transform into absolute first 
    abs_A = np.abs(A)
    # make sum of each column 
    column_sum = np.sum(abs_A , axis = 0) # axis = 0 ==> column sum
    return np.max(column_sum)

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line