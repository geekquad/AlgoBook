package main

import "fmt"

func flip(arr []int, i int) {
	temp, start := 0, 0
	for start < i { // flips elements from start to index i
		temp = arr[start]
		arr[start] = arr[i]
		arr[i] = temp
		start++
		i--
	}
}

func max(arr []int, size int) int {
	max := 0
	for i := 0; i < size; i++ {
		if arr[i] > arr[max] {
			max = i // max index
		}
	}
	return max
}

func pancakeSort(arr []int) {
	for n := len(arr); n > 1; n-- {
		max := max(arr, n)
		if max != n-1 {
			flip(arr, max) // flips max to first position
			flip(arr, n-1) // flips max to last position
		}
	}
}

func main() {
	temp := []int{12, 45, 78, 23, 56, 89, 34, 67, 90, 11, 25, 38,
		72, 94, 53, 61, 84, 29, 17, 66, 40, 82, 99, 13, 58, 74, 36,
		92, 19, 47}
	pancakeSort(temp)
	fmt.Println(temp)
}
