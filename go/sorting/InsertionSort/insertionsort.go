package insertionsort

import "fmt"

// InsertionSort : this method implements InsertionSort
func InsertionSort(list []int, size int) []int {
	fmt.Println("Sorting: ", list)
	for i := 1; i < size; i++ {
		j := i
		for j > 0 {
			if list[j-1] > list[j] {
				list[j-1], list[j] = list[j], list[j-1]
			}
			j--
		}
	}

	fmt.Println("Sorted!")
	return list
}

func main() {
	list := []int{432, 442, 126, 693, 356, 847, 1, 3452, 24, 13}

	sortedArray := InsertionSort(list, len(list))

	fmt.Println(sortedArray)
}
