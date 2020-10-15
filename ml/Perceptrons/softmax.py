# Softmax function

import numpy as np

def Softmax(z):     
    # The input for function sofmax is a vector
     
    return np.exp(z)/np.sum(np.exp(z),axis=0)