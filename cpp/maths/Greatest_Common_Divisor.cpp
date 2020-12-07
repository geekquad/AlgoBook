//Greatest common divisor
#include <iostream>
using namespace std;
//getting gcd of a and b using Euclidean Algo
int gcd(int a, int b)
{
    
    if (a == 0)
       return b;
    if (b == 0)
       return a;
  
    
    if (a == b)
        return a;
  
    
    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
}

int main()
{
    int a,b;
    cout<<"Enter the two numbers:";
    cin>>a>>b;
    cout<<"GCD of "<<a<<" and "<<b<<" is "<<gcd(a, b);
    return 0;
}
