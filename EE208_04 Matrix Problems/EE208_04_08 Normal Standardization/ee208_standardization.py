import numpy as np 

def column_standardization(X):
    # Step 1 : find column sample mean & sample std 
    sample_mean_col = np.mean(X , axis = 0) # axis = 0 : vertical 
    sample_std_col = np.std(X , axis = 0) # ddof = 1 for sample mean 
    
    # Step 2 : normalize 
    normalized_value = (X - sample_mean_col) / sample_std_col
    
    # return value
    return normalized_value # Return the standardized matrix

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line