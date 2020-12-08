#include<bits/stdc++.h> 
using namespace std; 
  
float APsum(float a, float d, float n) 
{ 
    float sum = (n / 2) * (2 * a + (n - 1) * d); 
    return sum; 
}  
int main() 
{ 
    float n,a,d; 
    cout<<"Enter first term "<<endl;
    cin>>a;
    cout<<"Enter no. of terms "<<endl;
    cin>>n;
    cout<<"Enter common difference"<<endl;
    cin>>d;

    cout<<endl<<"Sum of AP:"<<APsum(a, d, n); 
    return 0; 
} 