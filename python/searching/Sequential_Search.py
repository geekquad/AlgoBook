def Sequential_Search(datalist, item):

    pos = 0
    found = False
    
    while pos < len(datalist) and not found:
        if datalist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19,90,23,45,67,54,67],97))