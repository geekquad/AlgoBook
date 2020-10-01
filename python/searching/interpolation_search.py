list1=list(map(int ,input().split()))
val=int(input())
start=0
end=len(list1)-1
flag=0
while(start<=end and val>=list1[start] and val<=list1[end]):
    if(start==end):
        if list1[start] == val:
            print(start)
            flag=1
        else:
            print("-1")
    random= start + int(((float(end-start)/(list1[end]-list1[start]))*(val-list1[start])))

    if list1[random]==val:
        print(random)
        flag=1

    if list1[random]<val:
        start= random+1
    else:
        end= random-1
if(flag==0):
    print("-1")