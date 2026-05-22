import numpy as np 

def max_of_quadratic_function(X , A) : 
    # X_k is column of X 
    # X_k.T @ A @ X_k will return 1x1
    
    # find each value of X_k first
    
    quadratic_result = []
    
    # for loop indexing each column 
    for k in range(X.shape[1]) : # loop x until #col of x (shape[1])
        # define X_k representing each column vector in X
        X_k = X[: , k] # all row , column k 
        value = X_k.T @ A @ X_k
        # add value to list 
        quadratic_result.append(value)
        
    # change list to array 
    quadratic_result = np.array(quadratic_result)
    
    ## return maximum value
    return np.max(quadratic_result)

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line