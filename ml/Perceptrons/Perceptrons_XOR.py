import numpy as np
import pandas as pd

def step_function(value):
  if value >= 0:
    return 1
  else:
    return 0
  
def perceptron(x, weight, bias):
  v = np.dot(weight, x) + bias
  y = step_function(v)
  
  return y
def AND_perceptron(x):
  w = np.array([1,1])
  b = -1.5
  return perceptron(x, w, b)

def OR_perceptron(x):
  w = np.array([1,1])
  b = -0.5
  return perceptron(x, w, b)
  
def NOT_perceptron(x):
  return perceptron(x, weight=-1, bias=0.5)

print('NOT(1) = ', NOT_perceptron(1))
print('NOT(0) = ', NOT_perceptron(0))

input_binarylogics = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

def XOR_perceptron(x):
    gate_1 = AND_perceptron(x)
    gate_2 = NOT_perceptron(gate_1)
    gate_3 = OR_perceptron(x)
    new_x = np.array([gate_2, gate_3])
    output = AND_perceptron(new_x)
    
    return output
  
output_XOR = []
  
 
for input in input_binarylogics:
  result = XOR_perceptron(input)
  output_XOR.append(result)
        
output_binarylogics_XOR = np.array(output_XOR)

XOR_table = pd.DataFrame({'Input 1':input_binarylogics[:,0], 
                          'Input 2':input_binarylogics[:,1],
                          'Output':output_binarylogics_XOR})

#XOR_table (print this)
