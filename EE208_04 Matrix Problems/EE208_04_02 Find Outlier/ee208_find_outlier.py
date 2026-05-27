import numpy as np
from numpy import number
from numpy.typing import NDArray, ArrayLike
from typing import Annotated, Literal, Tuple, Callable
import matplotlib.pyplot as plt

Matrix2D = NDArray[number]
Vector = Array = Annotated[NDArray[number], Literal["N"]]

import numpy as np 

def find_outliers(x: Array, alpha: float) -> Array:
    # using np.percentile to get data from P25 to P75
    Q1 , Q3 = np.percentile(x , [25,75])
    IQR = Q3 - Q1
    
    # define bound of lower & upper
    lower_bound = alpha * (Q1)
    upper_bound = alpha * (Q3)
    
    # cap data with range (lies outside = (<Q1 , >Q3) )
    filtered_data = x[ (x <= lower_bound) | (x >= upper_bound) ] # Union = OR
    
    # sort data then return array 
    return np.sort(filtered_data) # Return the sorted outliers

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line