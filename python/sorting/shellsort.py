# shell sort in python 
# Shell Sort involves sorting elements which are away from ech other.

def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp


        gap = gap//2

list = [19,2,31,45,30,11,121,27]

shellSort(list)
print(list)