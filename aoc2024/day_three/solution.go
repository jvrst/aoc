package day_three

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	UNDEFINED = 0
	ASC       = 1
	DESC      = 2
)

func Solution() {
	file, err := os.ReadFile("./inputs/03.in")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(file), "\n")

	part1(lines)
	part2(lines)
}

func part1(input []string) {
	fmt.Println("part1")
	lst := [][2]int{}
	for _, line := range input {
		r, _ := regexp.Compile(`mul\((\d+),(\d+)\)`)
		matches := r.FindAllStringSubmatch(line, -1)
		enabled := true
		for _, match := range matches {
			fmt.Println(match)
			if match[0] == "do()" {
				fmt.Println("enabled", enabled)
				enabled = true
			}
			if match[0] == "don't()" {
				fmt.Println("disabled", enabled)
				enabled = false
			}
			if enabled {
				x, _ := strconv.Atoi(match[1])
				y, _ := strconv.Atoi(match[2])
				fmt.Println("enabled", enabled, x, y)
				lst = append(lst, [2]int{x, y})
			}
		}
	}
	fmt.Println(lst)

	sum := 0
	for _, l := range lst {
		sum += l[0] * l[1]
	}
	fmt.Println("part1", sum)
}

func part2(input []string) {
	fmt.Println("part2")

	lst := [][2]int{}
	enabled := true
	for _, line := range input {
		r, _ := regexp.Compile(`do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)`)
		matches := r.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			fmt.Println(match)
			if match[0] == "do()" {
				fmt.Println("enabled", enabled)
				enabled = true
			}
			if match[0] == "don't()" {
				fmt.Println("disabled", enabled)
				enabled = false
			}
			if enabled {
				x, _ := strconv.Atoi(match[1])
				y, _ := strconv.Atoi(match[2])
				fmt.Println("enabled", enabled, x, y)
				lst = append(lst, [2]int{x, y})
			}
		}
	}
	sum := 0
	for _, l := range lst {
		sum += l[0] * l[1]
	}
	fmt.Println("part2", sum)
}
