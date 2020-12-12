#include <iostream>
using namespace std;


int main()
{
    cout << "Enter a number:" <<endl;
    long long int num , d;
    cin >> num;
    long long int sum , copy_num;
    
    sum = 0;
    copy_num = num;

    while(copy_num !=0){
        d = copy_num%10;
        sum = sum + d;
        copy_num = copy_num/10;
    }

    cout << "Sum of digits of " << num << " = " << sum;

    return 0;
}
