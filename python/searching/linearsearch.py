def linearsearch(llist,key):
    for i in range(len(llist)):
        if llist[i]==key:
            return i+1 #return the position of the key in the list
    return -1 #return -1 if key not found

llist=[int(x) for x in input().split()]
key=int(input())
position=linearsearch(llist,key)
if position>0:
    print(key,"found at position",position)
else:
    print("Not Found!")
