package main

import "fmt"

func pigeonSort(arr []int) {
	min, max := arr[0], arr[0]
	for _, value := range arr { // finds max and min of slice
		if value < min {
			min = value
		} else if value > max {
			max = value
		}
	}
	r := max - min + 1
	holes := make([][]int, r) // creates holes
	for i := 0; i < len(arr); i++ {
		holes[arr[i]-min] = append(holes[arr[i]-min], arr[i])
	}
	index := 0
	for i := 0; i < r; i++ { // puts holes into original slice
		for _, value := range holes[i] {
			arr[index] = value
			index++
		}
	}
}

func main() {
	temp := []int{47, 82, 19, 63, 28, 94, 15, 76, 54, 33,
		88, 6, 72, 51, 98, 14, 39, 60, 25, 91, 3, 69, 22}
	pigeonSort(temp)
	fmt.Println(temp)
}
