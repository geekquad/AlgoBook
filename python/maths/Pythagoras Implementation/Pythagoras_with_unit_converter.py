# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:58:20 2020

@author: Vijay
"""
from math import sqrt

print("Pythagoras Theorem")

print("Sides of the Triangle are as :- \n 'h' for 'hypotenuse'\n 'p' for 'perpendicular'\n 'b' for 'base'.")

def converter(num,unit):
    num_unit = num.split(' ')
    if len(num_unit) == 1:
        return float(num)
    
    if num_unit[1] == unit:
        return float(num_unit[0])
    
    elif unit == 'm' and num_unit[1] == 'cm':
        num_unit[0] = float(num_unit[0])/100
        num_unit[1] = unit
        return float(num_unit[0])
    
    elif unit == 'm' and num_unit[1] == 'mm':
        num_unit[0] = float(num_unit[0])/1000
        num_unit[1] = unit
        return float(num_unit[0])
    
        
    elif unit == 'cm' and num_unit[1] == 'm':
        num_unit[0] = float(num_unit[0])*100
        num_unit[1] = unit
        return float(num_unit[0])
    
        
    elif unit == 'cm' and num_unit[1] == 'mm':
        num_unit[0] = float(num_unit[0])/10
        num_unit[1] = unit
        return float(num_unit[0])

        
    elif unit == 'mm' and num_unit[1] == 'm':
        num_unit[0] = float(num_unit[0])*1000
        num_unit[1] = unit
        return float(num_unit[0])

    elif unit == 'mm' and num_unit[1] == 'cm':
        num_unit[0] = float(num_unit[0])*10
        num_unit[1] = unit
        return float(num_unit[0])


while 1:
    side = input('Which side(h,p,b) do you want to calculate or enter exit :')

    
    
    if side == 'h':
        side_p_unit = input('Enter the lenght of Perpendicular(eg: x cm or x) : ')
        side_b_unit = input('Enter the lenght of Base(eg: y cm or y) : ')
        unit = input('In what unit(cm,m,mm) do you want the answer :')
        side_p = converter(side_p_unit,unit)
        side_b = converter(side_b_unit, unit)
        side_h = sqrt(side_p*side_p + side_b*side_b)
    
        print("The lenght of Hypotenuse is : {}".format(round(side_h,2)), unit)
        break
    
    elif side == 'p':
        side_h_unit = input('Enter the lenght of Hypotenuse(eg: x cm or x) : ')
        side_b_unit = input('Enter the lenght of Base(eg: y cm or y) : ')
        unit = input('In what unit(cm,m,mm) do you want the answer :')
        side_h = converter(side_h_unit,unit)
        side_b = converter(side_b_unit, unit)
        
        side_p = sqrt((side_h*side_h) - (side_b*side_b))
    
        print("The lenght of Perpendicular is : {}".format(round(side_p,2)),unit)
        break

    elif side == 'b':
        side_h = float(input('Enter the lenght of Hypotenuse : '))
        side_p = float(input('Enter the lenght of Perpendicular : '))
        
        side_h_unit = input('Enter the lenght of Hypotenuse(eg: x cm or x) : ')
        side_p_unit = input('Enter the lenght of Perpendicular(eg: y cm or y) : ')
        unit = input('In what unit(cm,m,mm) do you want the answer :')
        side_p = converter(side_p_unit,unit)
        side_h = converter(side_h_unit, unit)
    
        side_b = sqrt((side_h*side_h) - (side_p*side_p))
    
        print("The lenght of Perpendicular is : {}".format(round(side_p,2)), unit)
        break
    
    elif side =='exit':
        break
    
    else :
        print("Please enter valid side.")
        continue
