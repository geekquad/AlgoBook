# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:58:20 2020

@author: Vijay
"""
from math import sqrt

print("Pythagoras Theorem")

print("Sides of the Triangle are as :- \n 'h' for 'hypotenuse'\n 'p' for 'perpendicular'\n 'b' for 'base'.")


while 1:
    side = input('Which side(h,p,b) do you want to calculate or enter exit : ')

    
    
    if side == 'h':
        side_p = float(input('Enter the lenght of Perpendicular : '))
        side_b = float(input('Enter the lenght of Base : '))
    
        side_h = sqrt(side_p*side_p + side_b*side_b)
    
        print("The lenght of Hypotenuse is : {}".format(round(side_h,2)))
        break
    
    elif side == 'p':
        side_h = float(input('Enter the lenght of Hypotenuse : '))
        side_b = float(input('Enter the lenght of Base : '))
    
        side_p = sqrt((side_h*side_h) - (side_b*side_b))
    
        print("The lenght of Perpendicular is : {}".format(round(side_p,2)))
        break

    elif side == 'b':
        side_h = float(input('Enter the lenght of Hypotenuse : '))
        side_p = float(input('Enter the lenght of Perpendicular : '))
    
        side_b = sqrt((side_h*side_h) - (side_p*side_p))
    
        print("The lenght of Perpendicular is : {}".format(round(side_b,2)))
        break
    
    elif side =='exit':
        break
    
    else :
        print("Please enter valid side.")
        continue
