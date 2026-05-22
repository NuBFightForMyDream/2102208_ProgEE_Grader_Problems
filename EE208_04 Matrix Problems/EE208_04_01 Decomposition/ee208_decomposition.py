import numpy as np 

def decomposition(X, c):
    
    ## X_k is column vector of X , C is constant 
    # summing each element = C1 X X.T + C2 X X.T + ...
    
    ## for loop each column to get each column 
    decomposed_result = np.zeros((X.shape[0] , X.shape[0])) # same size as A , shape nxn 
    
    for i in range(X.shape[1]) : # loop x until #col of x (shape[1])
        X_i = X[ : , i ] # all row , column i
        
        ## using np.outer for outer product 
        decomposed_result += c[i] * np.outer(X_i , X_i.T) ## cant use c[i] * X_i @ X_i.T
        
    # return result
    return decomposed_result

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
