package main

import "fmt"

func gnomeSort(arr []int) {
	i, n := 0, len(arr)
	for i < n {
		if i == 0 {
			i++
		}
		if arr[i] >= arr[i-1] {
			i++
		} else {
			arr[i], arr[i-1] = arr[i-1], arr[i]
			i--
		}
	}
}

func main() {
	temp := []int{14, 67, 22, 93, 8, 45, 31, 76, 54, 18}
	gnomeSort(temp)
	fmt.Println(temp)
}
