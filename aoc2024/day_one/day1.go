package day_one

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func Solution() {
	file, err := os.Open("./inputs/day1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lst1 := []int{}
	lst2 := []int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		r, _ := regexp.Compile("[0-9]+")
		res := r.FindAllString(scanner.Text(), -1)
		res1, _ := strconv.Atoi(res[0])
		res2, _ := strconv.Atoi(res[1])
		lst1 = append(lst1, res1)
		lst2 = append(lst2, res2)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// sort 1st list
	sort.Slice(lst1, func(i, j int) bool {
		return lst1[i] < lst1[j]
	})
	// sort 2nd list
	sort.Slice(lst2, func(i, j int) bool {
		return lst2[i] < lst2[j]
	})

	part1(lst1, lst2)
	part2(lst1, lst2)
}

func part1(lst1 []int, lst2 []int) {
	sum := 0
	for i, v := range lst1 {
		delta := v - lst2[i]
		if delta < 0 {
			delta = delta * -1
		}
		sum += delta
	}
	log.Println("Part 1:", sum)
}

func part2(lst1 []int, lst2 []int) {
	similarity_score := 0
	for _, v := range lst1 {
		for _, v2 := range lst2 {
			if v == v2 {
				similarity_score += v
			}
		}
	}
	log.Println("Part 2:", similarity_score)
}
