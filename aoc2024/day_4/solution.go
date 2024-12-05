package day_4

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func Solution() {
	file, err := os.ReadFile("./inputs/04.in")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(file), "\n")

	part1(lines)
	part2(lines)
}

func part1(input []string) {
}

func part2(input []string) {
}