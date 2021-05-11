package quicksort

import (
	"fmt"
	"math/rand"
)

//QuickSort uses quick sort to sort an array of integers
func QuickSort(list []int) []int {
	if len(list) < 2 {
        return list
    }
     
    left, right := 0, len(list)-1
     
    pivot := rand.Int() % len(list)
     
    list[pivot], list[right] = list[right], list[pivot]
     
    for i, _ := range list {
        if list[i] < list[right] {
            list[left], list[i] = list[i], list[left]
            left++
        }
    }
     
    list[left], list[right] = list[right], list[left]
     
    QuickSort(list[:left])
    QuickSort(list[left+1:])
     
    return list
}

func main() {
	list := []int{4324, 442, 422, 6931, 356, 84722, 1, 3452, 24, 13, 89, 0, -111}

	sortedArray := QuickSort(list)

	fmt.Println(sortedArray)
}
