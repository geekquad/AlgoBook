#include <bits/stdc++.h>
using namespace std;

// Shell sort
void ShellSort(int array[], int n) {
  // Rearrange elements at each n/2, n/4, n/8, ... gaps.
  for (int gap = n / 2; gap > 0; gap /= 2) {
    for (int i = gap; i < n; i += 1) {
      int temp = array[i];
      int j;
      for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
        array[j] = array[j - gap];
      }
      array[j] = temp;
    }
  }
}

// Print an array
void printArray(int array[], int size) {
  int i;
  for (i = 0; i < size; i++)
    cout << array[i] << " ";
  cout << endl;
}

int32_t main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int size;
    cout << "Enter the number of elements you want to sort: \n";
    cin >> size;
    int data[size];
    cout << "Enter the elements: \n";
    for (int i=0; i<size; i++){
        cin >> data[i];
    }
    ShellSort(data, size);
    cout << "Sorted array: \n";
    printArray(data, size);
}