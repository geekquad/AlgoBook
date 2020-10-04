def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos


search = input("Input number : ")


print(Sequential_Search([11,23,38,31,56,67,63,77,65,17],search))
