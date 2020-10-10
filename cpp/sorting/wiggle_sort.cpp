#include<iostream>
#include<vector>
#include<algorithm>
using namespace std; 

void display(int*array, int size) {
for(int value=0; value<size; value++)
cout << array[value] << " ";
cout << endl;
}
void swap(int *x, int *y) { 
    int temp = *x; 
    *x = *y; 
    *y = temp; 
} 
// Wiggle Sort -> {arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]}
void WiggleSort(int arr[], int n) 
{ 
    // Sort the input array 
    sort(arr, arr+n); 
    for (int i=0; i<n-1; i += 2) 
        swap(&arr[i], &arr[i+1]); 
} 
int main() {
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements value:" << endl;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  cout << "Array before Wiggle Sorting: ";
  display(arr, n);
  WiggleSort(arr, n);
  cout << "Array after Wiggle Sorting: ";
  display(arr, n);
}