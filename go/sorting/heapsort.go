package main

import "fmt"

func heapify(arr []int, n int, index int) {
	largest := index
	left := 2*index + 1
	right := 2*index + 2
	if left < n && arr[left] > arr[largest] { // left child > root
		largest = left
	}
	if right < n && arr[right] > arr[largest] { // right child > largest
		largest = right
	}
	if largest != index { // largest not root
		arr[index], arr[largest] = arr[largest], arr[index]
		heapify(arr, n, largest)
	}
}

func heapSort(arr []int) {
	n := len(arr)
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i) // build heap inplace
	}
	for i := n - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0) // extract elements from heap
	}
}

func main() {
	temp := []int{42, 17, 88, 3, 56, 29, 74, 91, 10, 65}
	heapSort(temp)
	fmt.Println(temp)
}
