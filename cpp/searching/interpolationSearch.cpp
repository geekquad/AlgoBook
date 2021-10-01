#include<bits/stdc++.h>
using namespace std;

int interpolationSearch(int arr[],int lo,int hi,int x)

{
  int pos;
  if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
    pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));
    if (arr[pos] == x)
      return pos;
    if (arr[pos] < x)
      return interpolationSearch(arr, pos + 1, hi, x);
    if (arr[pos] > x)
      return interpolationSearch(arr, lo, pos - 1, x);
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
  int index = interpolationSearch(arr, 0, n, x);
  if (index != -1)
    cout << "Element found at index " << index;
  else
    cout << "Element not found.";
  return 0;
}
