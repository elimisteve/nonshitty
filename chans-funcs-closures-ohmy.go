// Steve Phillips / elimisteve
// 2012.07.05

package main

import (
	"fmt"
)

func main() {
	const NUM_PIECES = 5
	ch := make(chan *func() int, NUM_PIECES)
	sumGen := func(min, max int) *func() int {
		// nums stores all numbers in [min, max)
		nums := []int{}
		for i := min; i < max; i++ {
			nums = append(nums, i)
		}
		// summer sums all numbers in nums
		summer := func() (total int) {
			for _, n := range nums {
				total += n
			}
			return
		}
		return &summer
	}
	// Carve up [0..1000) into NUM_PIECES pieces
	size := 200
	for i := 0; i < NUM_PIECES; i++ {
		// Pass summer funcs to ch
		go func(j int) {
			ch <- sumGen(size*j, size*(j+1))
		}(i)
	}
	// Print the sums
	for i := 0; i < NUM_PIECES; i++ {
		f := <-ch
		fmt.Printf("Sum #%d: %d\n", i+1, (*f)())
	}
}
