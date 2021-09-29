N=1000001
a=[0]*N
s=[0]*(4*N)
lazy=[0]*(4 *N)
def build(l,r,p):
    if l>r:
        return None
    if l==r:  
        s[p]=a[l]
        return None
    m=(l+r)//2
    build(l,m,2*p+1)
    build(m+1,r,2*p+2)
    s[p]=s[2*p+1]+s[2*p+2]

def update(l,r,i,j,p,v):
    if lazy[p]!=0:
        s[p]+=(r-l+1)*lazy[p]
        if l!=r:
               lazy[2*p+1]+=lazy[p]
               lazy[2*p+2]+=lazy[p]
        lazy[p]=0
    if l>r or r<i or l>j :        #no overlap
        return
    if (l>=i and r<=j) :         #complete overlap
        s[p]+=(r-l+1)*v
        if l!=r:
            lazy[2*p+1]+=v
            lazy[2*p+2]+=v
        return 
    m=(l+r)//2
    update(l,m,i,j,2*p+1,v)
    update(m+1,r,i,j,2*p+2,v)
    s[p]=s[2*p+1]+s[2*p+2]
def query(l,r,i,j,p):
    if (l>r or r<i or l>j) : 
         return 0
    if lazy[p]!=0 :
        s[p]+=(r-l+1)*lazy[p]
        if l!=r:
            lazy[2*p+1]+=lazy[p]
            lazy[2*p+2]+=lazy[p]
        lazy[p]=0
    if (l>=i and r<=j) :
        return s[p]
    m=(l+r)//2
    ans=query(l,m,i,j,2*p+1)
    ans1=query(m+1,r,i,j,2*p+2)
    return ans+ans1
def main():
    n,c=map(int,input().split())
    build(0,n-1,0)
    x=y=z=val=0
    for i in range(c):
        g=list(map(int,input().split()))
        x=g[0]
        if x==0:
            y=g[1]
            z=g[2]
            val=g[3]
            update(0,n-1,y,z,0,val)
        else :
            y=g[1]
            z=g[2]
            print(query(0,n-1,y,z,0))
if __name__=='__main__':
    t=int(input())
    while t>0:
        main()
        t-=1
