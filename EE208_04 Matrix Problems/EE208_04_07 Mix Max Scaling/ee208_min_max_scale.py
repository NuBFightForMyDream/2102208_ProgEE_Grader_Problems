import numpy as np 
def column_min_max_scaling(X):
    # formula : x - min_col / max_col - min_col
    
    ## Step 1 : define min & max of each column 
    min_col = np.min(X , axis = 0)
    max_col = np.max(X , axis = 0)
    
    ## Step 2 : scale woth formula 
    return (X - min_col) / (max_col - min_col)
    
exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
