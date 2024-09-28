package main

import "fmt"

func selectionSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		min := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[min] {
				min = j
			}
		}
		if min != i {
			arr[min], arr[i] = arr[i], arr[min]
		}
	}
}

func main() {
	temp := []int{42, 7, 19, 88, 53, 26, 91, 34, 75, 61}
	selectionSort(temp)
	fmt.Println(temp)
}
