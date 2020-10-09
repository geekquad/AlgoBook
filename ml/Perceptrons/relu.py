# ReLu function 

import numpy as np

def relu(z):
    """
    Implements the relu function

    Parameters:
        vector (np.array,list,tuple): A  numpy array of shape (1,n)
        consisting of real values or a similar list,tuple


    Returns:
        relu_vec (np.array): The input numpy array, after applying
        relu.
    """
    
    # compare two arrays and then return element-wise maxima
    return np.maximum(0,z) 
