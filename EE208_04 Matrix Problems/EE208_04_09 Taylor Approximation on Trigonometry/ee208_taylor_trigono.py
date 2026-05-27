import numpy as np
import math 

def sincos_truncate(x,n):
    '''
    ## for sine function 
    sin_x = 0 # initial value 
    for expo in range(n) : # expo = 0,1,2,...,n-1 : k = 1,3,5,...,2n-1
        sin_x += ((-1) ** expo) * (x ** (2 * expo + 1)) / math.factorial((2 * expo + 1))
    
    ## for cosine function 
    cos_x = 0
    for expo in range(n) : # expo = 0,1,2,...,n-1 : k = 0,2,4,6,...,2n-2
        sin_x += ((-1) ** expo) * (x ** (2 * expo)) / math.factorial((2 * expo))

    ## return result
    return sin_x, cos_x
    '''
    
    sin_x = 0.0
    cos_x = 0.0

    sin_term = x
    cos_term = 1.0

    for k in range(n):

        sin_x += sin_term
        cos_x += cos_term

        # using recurrence relation for not overflowing
        sin_term *= -(x * x) / ((2*k + 2) * (2*k + 3))
        cos_term *= -(x * x) / ((2*k + 1) * (2*k + 2))

    ## return result
    return round(sin_x , 4) , round(cos_x , 4)

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line