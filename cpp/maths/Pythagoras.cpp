#include <iostream>
#include <math.h>                 
using namespace std;

int main ()
{
    float a, b, result;
    if ((a > 0) && (b > 0)); 
       {
       cout << "Input the lengths of the two sides"<<endl;
       cin >> a >> b;
       result = sqrt((a*a)+(b*b));
       cout << "\n The hypotenuse length is: " << (result);
       }
       return 0;
}