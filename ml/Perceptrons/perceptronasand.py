import numpy as np
## step-function
def step(vec):
    """ returns 1 when true and 0 when false """
    if vec >= 0 :
        return 1
    else:
        return 0
## perceptron model
def perceptron(x, w, b):
    """ defining the perceptron model
        x = Inputs
        w = weights
        b = bias
    """
    vec = np.dot(w, x) + b
    y = step(vec)
    return y
## AND function
def AND_gate(x):
    """ defining the AND Logic Gate
    w1 = 1.0
    w2 = 1.0
    b = -2.0
    """
    w = np.array([1,1])
    b = -2.0
    return perceptron(x, w, b)
## TESTING
t1 = np.array([0, 1])
t2 = np.array([1, 1])
t3 = np.array([0, 0])
t4 = np.array([1, 0])
## Displaying Results
print("AND({}, {}) = {}".format(0, 1, AND_gate(t1)))
print("AND({}, {}) = {}".format(1, 1, AND_gate(t2)))
print("AND({}, {}) = {}".format(0, 0, AND_gate(t3)))
print("AND({}, {}) = {}".format(1, 0, AND_gate(t4)))