#include <iostream>
using namespace std;

//*Find whether or not there exists any subset of array  that sum up to targetSum
//function call
bool subset_sum_BT(int arr[], int pos, int sum, int temp, int size){
    bool stat = false;
    if(sum==temp){
        //base condition
        stat = true;
        return stat;
    }
    // generate nodes along the breadth
    else{
        for(int i=pos; i<size; i++){
            if(temp + arr[i] <= sum){
                //adding elements to temp
                temp += arr[i];
                subset_sum_BT(arr, i+1, sum, temp, size);               // consider next level node (along depth)
                temp -= arr[i];
            }
        }
    }
}

int main(){
    int n,sum;
    cout<<"enter no of elements:  ";
    cin >> n;  
                                                //taking input
    int arr[n];
    cout << "enter array elements:"<<endl;
    for(int i=0; i<n; i++){
        cin >> arr[i];                          //taking input for array elements
    }

    cout << "enter sum:  ";                     //required sum
    cin >> sum;     
    bool B = subset_sum_BT(arr, 0, sum, 0, n);      //function call
    if(B)
        cout << "found the sum" <<endl;
    else
        cout <<"Not found!!!"<<endl;
    return 0;
}
