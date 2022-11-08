void countingSort(int v[], int n) {

  int max = v[0];
  for (int i = 1; i < n; i++) {
    if (v[i] > max)
      max = array[i];
  }

  int count[max+1];

  for (int i = 0; i <= max; i++) {
    count[i] = 0;
  }

  for (int i = 0; i < n; i++) {
    count[v[i]]++;
  }

  for (int i = 1; i <= max; i++) {
    count[i] += count[i - 1];
  }

  for (int i = n - 1; i >= 0; i--) {
    count[v[i]] - 1 = v[i];
    count[v[i]]--;
  }
}
