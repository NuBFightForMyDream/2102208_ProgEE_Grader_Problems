import numpy as np 

def matrix_norm(d, v, A):
    
    # change d,v to diagonal first 
    D = np.diag(d)
    V = np.diag(v) 
    
    # return result with matrix multiplication
    return D @ A @ V.T # transpose

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line