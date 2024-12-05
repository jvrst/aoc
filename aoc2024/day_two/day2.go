package day_two

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

const (
	UNDEFINED = 0
	ASC       = 1
	DESC      = 2
)

func Solution() {
	file, err := os.Open("./inputs/02.in")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lst := [][]int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		r, _ := regexp.Compile("[0-9]+")
		res := r.FindAllString(scanner.Text(), -1)
		tmp := []int{}
		for _, n := range res {
			x, _ := strconv.Atoi(n)
			tmp = append(tmp, x)
		}
		lst = append(lst, tmp)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// part1(lst)
	part2(lst)
}

func part1(lst [][]int) {
	fmt.Println(lst)
	cnt := 0
	for _, l := range lst {
		if isSafe(l) {
			cnt += 1
		}
		fmt.Println(l, isSafe(l))
	}
	log.Println(cnt)
}

func part2(lst [][]int) {
	cnt := 0
	for _, l := range lst {
		if isSafeDampened(l) {
			cnt += 1
		}
		fmt.Println(l, isSafeDampened(l))
	}

	log.Println(cnt)
}

func isSafe(lst []int) bool {
	var order int
	prev := 9999999999
	for _, curr := range lst {
		if prev == 9999999999 {
			prev = curr
			continue
		}

		if order == UNDEFINED {
			if curr-prev > 0 {
				order = ASC
			} else {
				order = DESC
			}
		}

		if order == ASC && curr-prev < 0 {
			fmt.Println("ASC", curr, prev)
			return false
		}

		if order == DESC && curr-prev > 0 {
			fmt.Println("DESC", curr, prev)
			return false
		}

		diff := curr - prev
		if diff < 0 {
			diff *= -1
		}

		if diff < 1 || diff > 3 {
			fmt.Println("DIFF", curr, prev, diff)
			return false
		}
		prev = curr
	}

	return true
}

func isSafeDampened(lst []int) bool {
	if isSafe(lst) {
		return true
	}

	lsts := removeOne(lst)
	for _, l := range lsts {
		if isSafe(l) {
			return true
		}
	}
	return false
}

// removeOne generates all possible slices where one element is removed
func removeOne(arr []int) [][]int {
	var result [][]int
	for i := range arr {
		// Create a new slice excluding the element at index i
		newSlice := append([]int{}, arr[:i]...)
		newSlice = append(newSlice, arr[i+1:]...)
		result = append(result, newSlice)
	}
	return result
}
