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
    double x;
    
    // summation of all terms
    for (int i = 1; i < n; i++) {
      x = a + i*h;
        if(i%3==0){
        result += 2*func(x); 
       }
    else {  
         result += 3*func(x); 
      }
    }
    // counting of integral
    result = 3*h*result;
    result = result/8;
    return result;
}

double func(double x)
{
  return 1/(1+x*x);//function
}
