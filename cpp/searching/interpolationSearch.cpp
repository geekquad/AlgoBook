#include<bits/stdc++.h>

using namespace std;

int interpolationSearch(int arr[], int n, int x) {

  int low = 0, hi = (n - 1);
  while (low <= hi && x >= arr[low] && x <= arr[hi]) {
    if (low == hi) {
      if (arr[low] == x) return low;
      return -1;
    }
    int pos = low + (((double)(hi - low) / (arr[hi] - arr[low])) * (x - arr[low]));
    if (arr[pos] == x)
      return pos;
    if (arr[pos] < x)
      low = pos + 1;

  int lo = 0, hi = (n - 1);
  while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
    if (lo == hi) {
      if (arr[lo] == x) return lo;
      return -1;
    }
    int pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));
    if (arr[pos] == x)
      return pos;
    if (arr[pos] < x)
      lo = pos + 1;
    else
      hi = pos - 1;
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
  int index = interpolationSearch(arr, n, x);
  if (index != -1)
    cout << "Element found at index " << index;
  else
    cout << "Element not found.";
  return 0;
}