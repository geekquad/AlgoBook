package main

import "fmt"

func merge(arr []int, left int, mid int, right int) {
	// two subarrays - arr[left:mid+1] and arr[mid+1:right+1]
	n1 := mid - left + 1
	n2 := right - mid
	l := make([]int, n1) // left slice
	r := make([]int, n2) // right slice
	// copies data into slices
	for i := 0; i < n1; i++ {
		l[i] = arr[left+i]
	}
	for j := 0; j < n2; j++ {
		r[j] = arr[mid+1+j]
	}
	i, j, k := 0, 0, left
	for i < len(l) && j < len(r) {
		if l[i] <= r[j] {
			arr[k] = l[i]
			i++
		} else {
			arr[k] = r[j]
			j++
		}
		k++
	}
	for i < len(l) { // copies remaining left elements
		arr[k] = l[i]
		i++
		k++
	}
	for j < len(r) { // copies remaining right elements
		arr[k] = r[j]
		j++
		k++
	}
}

func mergeSortHelper(arr []int, left int, right int) {
	if left >= right {
		return
	}
	mid := left + (right-left)/2
	mergeSortHelper(arr, left, mid)
	mergeSortHelper(arr, mid+1, right)
	merge(arr, left, mid, right)
}

func mergeSort(arr []int) { mergeSortHelper(arr, 0, len(arr)-1) }

func main() {
	temp := []int{27, 3, 45, 18, 92, 56, 12, 78, 34, 81, 66, 24, 9, 43, 71}
	mergeSort(temp)
	fmt.Println(temp)
}
