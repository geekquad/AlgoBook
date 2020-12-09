//Extended Euclidean Algorithm 
//It has extra variables to compute ax + by = gcd(a, b).
#include <bits/stdc++.h>
using namespace std;
int ExtendedGCD(int a, int b, int *x, int *y) {
   if (a == 0) {
      *x = 0;
      *y = 1;
      return b;
   }
   int x1, y1;
   int gcd = ExtendedGCD(b%a, a, &x1, &y1);
   *x = y1 - (b/a) * x1;
   *y = x1;
   return gcd;
}
int main() {
   int x, y;
    int a,b;
    cout<<"Enter the two numbers:";
    cin>>a>>b;
   cout<<"GCD is "<<ExtendedGCD(a, b, &x, &y);
   return 0;
}
