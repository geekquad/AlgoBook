def binarysearch(llist,key):
    low=0
    high=len(llist)-1
    while(low<=high):
        mid=(low+high)//2
        if llist[mid]==key:
            return mid+1
        elif llist[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1 #it returns -1 if the key is not found
llist=[int(x) for x in input().split()]
key=int(input())
position=binarysearch(llist,key)
if position==-1:
    print("Not Found!")
else:
    print(key,"found at",position)
