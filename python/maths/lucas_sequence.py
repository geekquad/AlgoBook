# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:50:11 2020

@author: Vijay
"""

# Lucas Number using Recursion.

# Approach 1 ->

def lucas(num):
    
    # Base Cases ->
    if (num == 0) :
        return 2
    
    if (num == 1) :
        return 1
    
    # Recurrence Relation
    return lucas(num - 1) + lucas(num - 2)

num = int(input('Enter the Number -> '))

print("Lucas number is -> ", lucas(num) )

# Approach 2 ->

'''
def lucas(num , num_1 = 2, num_2 = 1):
    if num :
        return lucas(num - 1, num_2 ,num_1 + num_2)
    
    else:
        return num_1
    
    
num = int(input('Enter Number -> '))

print("Lucas Number is -> ", lucas(num)) 
'''

