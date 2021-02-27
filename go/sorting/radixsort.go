package radixsort

import (
	"fmt"
	"math"
	"strconv"
)

//RadixSort uses radix sort to sort an array of integers
func RadixSort(list []int) []int {
	fmt.Println("Sorting  ", list)
	max := Max(list)
	count := len(strconv.Itoa(max))
	i := 0
	for i < count {
		buckets := make([][]int, 10)
		for _, number := range list {
			divisor := int(math.Pow(10, float64(i)))
			digit := (number / divisor) % 10
			buckets[digit] = append(buckets[digit], number)
		}
		list = nil
		for _, bucket := range buckets {
			list = append(list, bucket...)
		}
		i++
	}
	return list
}

//Max returns the maximum integer in an array of integers
func Max(list []int) int {
	max := list[0]
	for _, num := range list[1:] {
		if num > max {
			max = num
		}
	}
	return max
}

func main() {
	list := []int{4324, 442, 422, 6931, 356, 84722, 1, 3452, 24, 13, 89, 0, 111}

	sortedArray := RadixSort(list)

	fmt.Println(sortedArray)
}
