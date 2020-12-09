#include<bits/stdc++.h>
using namespace std;
double val(vector<int>&func,double x){
    double ans=0;
    for(int i=0;i<(int)func.size();i++){
        ans+=func[i]*pow(x,(int)func.size()-i-1);
    }
    return ans;
}
//This function is used to find the value of the polynomial func at any value x
int main()
{
    vector<int>f,g;
    int n,step=0,N;
    double f1,x1,e,x0;
    cout<<"Enter the degree of the polynomial : ";
    cin>>n;
    //The degree of the polynomial will be n
    f.assign(n+1,0);
    g.assign(n,0);
    cout<<"Enter the coefficients of the polynomial (Descending order of degree)";
    for(int i=0;i<=n;i++){
        cin>>f[i];
    }
    //This vector holds the coefficients of the polynomial 
    //For examples if n=2, ax^2 + bx + c, vector will have {a,b,c}
    for(int i=0;i<n;i++){
        g[i]=(n-i)*f[i];
    }
    //This vector holds the coefficients of the derivative of the polynomial
    //Derivative for n=2 will be, 2ax + b, vector will have {2a,b}
    cout<<"Enter initial guess : ";
    cin>>x0;
    //The initial guess for the variable
    cout<<"Enter tolerable error : ";
    cin>>e;
    //Maximum error allowed in the final function
    cout<<"Enter maximum iteration : ";
    cin>>N;
    //Maximum number of iterations allowed
    do
    {
        double g0 = val(g,x0);
        //The value of the derivative at x=x0
        double f0 = val(f,x0);
        //The value of the functiom at x=x0
        if(g0 == 0.0)
        {
            cout<<"Mathematical Error.";
            //Denominator will become zero 
            exit(0);
        }
        x1 = x0 - f0/g0;
        //The guess for the variable x for the next iteration
        x0 = x1;
        //The next guess will become the initial guess for the next iteration
        step++;
        if(step > N)
        {
            cout<<"Not Convergent.";
            //If we take more steps than the allowed number of iterations
            exit(0);
        }
        f1 = val(f,x1);
    }while(fabs(f1)>e);//Once the accuracy of the answer becomes more than the tolerable error 
    cout<<"Root is: "<<fixed<<x1;
    //Final value of the root
    return 0;
}