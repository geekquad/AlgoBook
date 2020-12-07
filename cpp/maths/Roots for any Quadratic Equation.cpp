#include<bits/stdc++.h>

using namespace std;

int main()
{
    long double a,b,c,delta;
    cout<<"Enter coefficient of x^2:  ";
    cin>>a;
    cout<<"Enter coefficient of x:  ";
    cin>>b;
    cout<<"Enter constant:  ";
    cin>>c;
    delta= b*b-4*a*c;
    if(delta>=0)
    {
        cout<<"Roots of the equation are: "<< (-b+pow(delta,0.5))/2*a<<", "<<(-b-pow(delta,0.5))/2*a<<endl;
    }
    else{
        cout<<"Roots of the equation are: "<< -b/2*a <<" + i"<<pow(-delta,0.5)/2*a<<", "<<-b/2*a<<" - i"<<pow(-delta,0.5)/2*a<<endl;
    }
    return 0;
}
