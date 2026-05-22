import numpy as np 

def max_inner_product(A, x):
    # Note : a_k is column vector of A (having m diemnsion) 
    # transpose A then matmul with x -> returning nx1 dimension
    inner_product = A.T @ x
    return np.max(inner_product)

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line
