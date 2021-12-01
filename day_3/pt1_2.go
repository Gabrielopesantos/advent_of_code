package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// right 3 down 1
func pt1(dat []byte, right, down int) int {
	treesFound := 0
	currCol := 0
	s := strings.Split(string(dat), "\n")

	for i, row := range s[:len(s)-1] {
		var c int

		if i%down != 0 {
			continue
		}

		if currCol > 30 {
			c = currCol % 31
		} else {
			c = currCol
		}

		if string(row[c]) == "#" {
			treesFound++
		}
		currCol += right
	}

	return treesFound
}

func main() {
	dat, err := ioutil.ReadFile("input.txt")
	check(err)
	fmt.Println("pt1", pt1(dat, 3, 4))

	// pt2
	slopes := [][]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

	val_pt2 := 1
	for _, vals := range slopes {
		val_pt2 *= pt1(dat, vals[0], vals[1])
	}

	fmt.Println("pt2", val_pt2)
}
