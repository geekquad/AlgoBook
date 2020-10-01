#Interpolation search is an improved version of binary search.
#Its time complexity is O(log(log n)) as compared to log(n) of binary search.
#following is the code of interpolation search:

# Python program to implement interpolation search 
#Variable naming:
"""
1) lys - our input array
2) val - the element we are searching for
2) index - the probable index of the search element. This is computed to be a higher value when val
is closer in value to the element at the end of the array (lys[high]), and lower when val
is closer in value to the element at the start of the array (lys[low])
4) low - the starting index of the array
5) high - the last index of the array"""
  
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1
print(InterpolationSearch([1,2,3,4,5,6,7,8], 6))    