#include<bits/stdc++.h>
using namespace std;
double val(vector<int>&func,double x){
    double ans=0;
    for(int i=0;i<(int)func.size();i++){
        ans+=func[i]*pow(x,(int)func.size()-i-1);
    }
    return ans;
}
int main()
{
    vector<int>f,g;
    int n,step=0,N;
    double f1,x1,e,x0;
    cout<<"Enter the degree of the polynomial : ";
    cin>>n;
    f.assign(n+1,0);
    g.assign(n,0);
    cout<<"Enter the coefficients of the polynomial (Descending order of degree)";
    for(int i=0;i<=n;i++){
        cin>>f[i];
    }
    for(int i=0;i<n;i++){
        g[i]=(n-i)*f[i];
    }
    cout<<"Enter initial guess : ";
    cin>>x0;
    cout<<"Enter tolerable error : ";
    cin>>e;
    cout<<"Enter maximum iteration : ";
    cin>>N;
    do
    {
        double g0 = val(g,x0);
        double f0 = val(f,x0);
        if(g0 == 0.0)
        {
            cout<<"Mathematical Error.";
            exit(0);
        }
        x1 = x0 - f0/g0;
        x0 = x1;
        step++;
        if(step > N)
        {
            cout<<"Not Convergent.";
            exit(0);
        }
        f1 = val(f,x1);
    }while(fabs(f1)>e);
    cout<<"Root is: "<<fixed<<x1;
    return 0;
}