#include<bits/stdc++.h>
using namespace std;

int binarySearch(int arr[],int l,int r,int x){
  if (r >= l) {
    int mid = l + (r - l) / 2;
    if (arr[mid] == x)
      return mid;
    if (arr[mid] > x)
      return binarySearch(arr, l, mid - 1, x);
    return binarySearch(arr, mid + 1, r, x);
  }
  return -1;
}

int exponentialSearch(int arr[], int n, int x) {
  if (arr[0] == x)
    return 0;
  int i = 1;
  while (i < n && arr[i] <= x)
    i = i * 2;
  return binarySearch(arr, i / 2, min(i, n), x);
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
  int x;
  cout << "Enter the element to be searched: ";
  cin >> x;
  int index = exponentialSearch(arr, n, x);
  if (index != -1)
    cout << "Element found at index " << index;
  else
    cout << "Element not found.";
  return 0;
}