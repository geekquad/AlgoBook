#Interpolation search is an improved version of binary search.
#Its time complexity is O(log(log n)) as compared to log(n) of binary search.
#following is the code of interpolation search:

# Python program to implement interpolation search 
  
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