import numpy as np

def hankel_matrix(x):
    # This matrix is flip axis of diagonal from \ to /
    ## Easy way : using np.fliplr(np.diag(x)) can solve this problem
    
    # Step 0 : get array size from x (using np.shape) & reverse x 
    m_size = x.shape[0] # (row , col , ...) -> row
    x_reverse = x[::-1]
    
    # Step 1 : define zero array
    hankel_mat = np.zeros((m_size , m_size)) # nxn matrix
    
    # Step 2 : slicing member from matrix then replace in hankel_mat
    ## Note : slicing matrix with array[ row_slice , col_slice ]
    hankel_mat[ np.arange(0 , m_size , 1) , np.arange(m_size-1 , -1 , -1) ] = x_reverse  
    
    # return matrix 
    return hankel_mat # Return the resulting matrix

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
