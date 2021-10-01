


def new_stack(val):
    newl=[]
    newl.append(val)
    return newl

def patience_sort(t,n):
    ans=[]

    for j in range(n):
        mn=10000
        flag=0
        for i in range(len(t)):
            if len(t[i])>0:
                x=t[i].pop()
                if x<mn:
                    mn=x
                    l=i
                t[i].append(x)
        t[l].pop()
        if t[l]==0:
            t.pop(l)
        ans.append(mn)
        #print(f'level {j+1} has minimum value {mn}')
    for i in range(len(ans)):
        print(ans[i],end=" ")


if __name__=='__main__':
    n=int(input('Enter number of element you want: '))
    print('Enter space seperated values:  ')
    l=list(map(int,input().split()))
    fir=new_stack(l[0])
    t=[]
    t.append(fir)
   # print(len(t))
    for i in range(1,n):

        flag=0
        for j in range(len(t)):
            y=t[j].pop()
            if y>=l[i]:
                flag=1
                t[j].append(y)
                t[j].append(l[i])
                break
            else:
                t[j].append(y)
        if flag!=1:
            fir=new_stack(l[i])
            t.append(fir)
    print('Sorted list using patience sorting algorithm: ')
    patience_sort(t,n)
