package bogosort

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

// BogoSort : this method sorts the array using Bogo Sort
func BogoSort(list []int, size int) []int {
	rand.Seed(time.Now().UnixNano())
	fmt.Println("Sorting: ", list)
	arr := make([]int, size)
	copy(arr, list)
	for !sort.IntsAreSorted(arr) {
		for i, v := range rand.Perm(size) {
			arr[i] = list[v]
		}
	}

	fmt.Println("Sorted!")
	return arr
}

func main() {
	list := []int{432, 442, 126, 693, 356, 847, 1, 3452, 24, 13}

	sortedArray := BogoSort(list, len(list))

	fmt.Println(sortedArray)
}
