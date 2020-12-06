package bubblesort

import (
	"fmt"
)

// BubbleSort the method sorts the array using Bubble Sort
func BubbleSort(list []int, size int) []int {
	fmt.Println("Sorting: " + list)
	flag := true
	for flag {
		flag = false
		for i := 1; i < size; i++ {
			if list[size-1] > list[i] {
				list[i], list[i-1] = list[i-1], list[i]
				flag = true
			}
		}
	}

	fmt.Println("Sorted!")
	return list
}

func main() {
	list := []int{432, 442, 126, 693, 356, 847, 1, 3452, 24, 13}

	sortedArray := BubbleSort(list, len(list))

	fmt.Println(sortedArray)
}
