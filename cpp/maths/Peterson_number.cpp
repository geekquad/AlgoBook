
#include <iostream>
using namespace std;

int fact(int n){
	  if(n > 1)
        return n * fact(n - 1);
    else
        return 1;
}

bool peterson(int n)
{
    int num = n, sum = 0;
    while (n > 0) {
        int digit = n % 10;
        int factorial=fact(digit);
        sum += factorial;
        n = n / 10;
    }
    return (sum == num);
}

int main()
{
    int n;
    cout<<"Enter a number";
    cin>>n;
    if (peterson(n))
        cout << "Yes";
    else
        cout << "No";
    return 0;
}