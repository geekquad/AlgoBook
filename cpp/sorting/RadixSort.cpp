//This is a program to sort numbers by using Radix Sort Algorithm;

/*• Main idea
– Break key into “digit” representation
key =  id, id-1, …, i2, i1.

– "digit" can be a number in any base, a character, etc
• Radix sort:
for i= 1 to d
 sort “digit” i using a stable sort
• Analysis : O(d *(stable sort time)) where d is the number of “digit”s

• Which stable sort?
– Since the range of values of a digit(0-9) is small the
best stable sort to use is Counting Sort which is usually not stable but we are modifying it here to make it stable.

*/

#include <iostream>

using namespace std;

void print(int*arr,int n){//Function to print numbers in array;

for(int i=0;i<n;i++){
    cout<<arr[i]<<" ";
}

}

int FindMax(int* arr,int n){//Function to find the maximum number in an array.

int maxnumber=arr[0];

for(int i=0;i<n;i++){

    if(arr[i]>maxnumber){
            maxnumber=arr[i];
        }
}

return maxnumber;

}


void CountingSort(int *arr,int n,int k){

int countarr[10]={0};//Creating array to store count of digits and initializing them with 0;

for(int i=0;i<n;i++){

     countarr[(arr[i] / k) % 10]++;//(arr[i]/k)%10 represents the digits from right to left individually .
}

for(int i=0;i<9;i++){
    countarr[i+1]=countarr[i]+countarr[i+1];//Modifying the count array so that it contains the sum of two previous count.
}


int temparr[n];//Creating a temporary array to store the sorted numbers according the the digit selected currently.

for(int i=n-1;i>=0;i--){ //Modified Counting sort which is stable.
     temparr[countarr[(arr[i] / k) % 10] - 1] = arr[i];//Sorting the numbers and storing them in temporary array.
}

// Copy the  temporary array to arr[], so that arr[] now
// contains sorted numbers according to current digit
 for (int i = 0; i < n; i++){
        arr[i] = temparr[i];
}


}

void RadixSort(int *arr,int n){

    int maxnumber=FindMax(arr,n);//This is done to figure out the max no. of digits required to compare.

    for(int i=1;(maxnumber/i)>0;i=i*10){//We are passing exponential value for Counting sort to sort digit by digit from unit's place and so on to the right..

        CountingSort(arr,n,i);
    }

}


int main()
{
 int n;

cout<<"Enter the size of array"<<endl;

cin>>n;

  int *arr=new int[n];//Dynamically creating an array of input size n;

cout<<"Enter the numbers"<<endl;

 for(int i=0;i<n;i++){//Taking  input in array;
cin>>arr[i];

 }

RadixSort(arr,n);//Calling Radix Sort

print(arr,n);//Printing the sorted numbers

}
