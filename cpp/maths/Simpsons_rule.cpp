#include <iostream>
#include<math.h>
using namespace std;

double simpsons(double a, double b, int n);
double func(double x);

int main()
{
     double low; // Lower limit 
     double up; // Upper limit 
     int n; // Number of interval 
     /* Input */
     cout<<"Enter lower limit of integration: ";
     cin>>low;
     cout<<"Enter upper limit of integration: ";
     cin>>up;
     cout<<"Enter number of intervals: ";
     cin>>n;
     cout<< endl <<"Required value of integration is: "<< simpsons(low, up, n);
     return 0;
}

double simpsons(double a, double b, int n)
{
    double result= 0;
    double h = (b - a) / n; // finding h base length
    result+= func(a);
    result+= func(b);
    // summation of all odd terms
    for (int i = 1; i < n; i+=2) {
        result += 4*func(i*h); 
    }
    // summation of all odd terms
    for (int i = 2; i < n; i+=2) {  
         result += 2*func(i*h); 
    }
    
    // counting of integral
    result = h / 3 * result;
    return result;
}

double func(double x)
{
  return 1/(1+x*x);//function
}
