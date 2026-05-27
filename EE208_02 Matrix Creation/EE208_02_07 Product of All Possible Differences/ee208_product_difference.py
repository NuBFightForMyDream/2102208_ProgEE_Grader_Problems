import numpy as np 
def product_of_all_possible_differences(t):
    # define product value 
    product_value = 1 
    
    # for loop each element in t
    for i in range(t.shape[0] - 1) : 
        # slicing for product 
        current = t[i]
        slice_next = t[i+1 : ]
        
        # subtract for difference
        difference = current - slice_next 
        
        # use np.product to find product of possible diff
        product_value *= np.prod(difference)
        
    return product_value # Return the product as a floating-point number

exec("\n".join(iter(input, "#Exit"))) # Don’t remove this line