import numpy as np 
def is_prime(n: int) -> bool:
     
    # check if number < 2 first
    if n < 2 : return False 
    
    # loop num until sqrt(num) 
    for divider in range(2 , int(n ** 0.5) + 1) :
        if (n % divider == 0) : 
            return False 

    return True # if no number divided , it's prime number
    
    

if __name__ == "__main__":
    # You can test anything inside this block and can send it to grader
    # The grader will use only the function that you have implemented
    # !!! DO NOT write anything outside this block
    print(is_prime(3))
    print(is_prime(10))