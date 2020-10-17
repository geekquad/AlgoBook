#include<bits/stdc++.h>
using namespace std;

int ternarySearch(int start,int length,int key,int ar[]){
  if (length >= start) {
    int mid1 = start + (length - start) / 3;
    int mid2 = length - (length - start) / 3;
    if (ar[mid1] == key) {
      return mid1;
    }
    if (ar[mid2] == key) {
      return mid2;
    }
    if (key < ar[mid1]) {
      return ternarySearch(start, mid1 - 1, key, ar);
    } else if (key > ar[mid2]) {
      return ternarySearch(mid2 + 1, length, key, ar);
    } else {
      return ternarySearch(mid1 + 1, mid2 - 1, key, ar);
    }
  }
  return -1;
  
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
  //0 is starting index
  int index = ternarySearch(0, n, x, arr);
  if (index != -1)
    cout << "Element found at index " << index;
  else
    cout << "Element not found.";
  return 0;
}