#include <iostream>
using namespace std;

// Recursive function to return Greatest Common Divisor of a and b
long long greatest_common_divisor(long long int a, long long int b)
{
    if (b == 0)
        return a;
    return greatest_common_divisor(b, a % b);
}

// Function to return LCM of two numbers
long long lcm(int a, int b)
{
    int least_common_multiple = (a / greatest_common_divisor(a, b)) * b ;
        return least_common_multiple ;
}

int main()
{
    cout << "Enter two numbers:" <<endl;
    int num1, num2;
    cin >> num1 >> num2;
    long long int least_common_multiple = lcm(num1, num2);

    cout << "LCM of " << num1 << " and "
         << num2 << " is " << least_common_multiple;

    return 0;
}

