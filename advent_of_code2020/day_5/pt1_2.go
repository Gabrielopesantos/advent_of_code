package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strings"
)

//  ROW  COL
// XXXXX YYY

type Seat struct {
	row, col int
}

func (s Seat) calcSeatID() int {
	return s.row*8 + s.col
}

// func Find(slice []int, val int) bool {
// 	for _, sval := range slice {
// 		if val == sval {
// 			return true
// 		}
// 	}

// 	return false
// }

func generateFirstLastRowsIds() []int {
	allIds := make([]int, 0)
	rows := []int{0, 127}

	for _, row := range rows {
		for col := 0; col < 8; col++ {
			allIds = append(allIds, row*8+col)
		}
	}

	return allIds
}

func getMax(intLst []int) (highest int) {
	for _, val := range intLst {
		if val > highest {
			highest = val
		}
	}

	return
}

func bin_search(pos []string, chars []string, upperB float64) float64 {
	var lowerB float64

	for _, c := range chars {
		switch c {
		case pos[0]:
			lowerB = math.Round((lowerB + upperB) / 2)
		case pos[1]:
			upperB = math.Floor((lowerB + upperB) / 2)
		default:
			fmt.Println("\n", c, "?")
		}
	}

	if chars[len(chars)-1] == pos[0] {
		return upperB
	} else {
		return lowerB
	}
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	seatIDS := make([]int, 0)
	cols_pos := []string{"R", "L"}
	rows_pos := []string{"B", "F"}

	dat, err := ioutil.ReadFile("input.txt")
	check(err)

	seatsCode := strings.Split(string(dat), "\n")

	for _, code := range seatsCode[:len(seatsCode)-1] {
		code_b := strings.Split(code, "")

		seatIDS = append(seatIDS, Seat{row: int(bin_search(rows_pos, code_b[:7], 127)), col: int(bin_search(cols_pos, code_b[7:], 7))}.calcSeatID())
	}
	fmt.Println(getMax(seatIDS))

	followsRule := make([]int, 0)

	sort.Ints(seatIDS)
	for i, val := range seatIDS {
		if i < len(seatIDS)-2 {
			if seatIDS[i+1]-val == 2 {
				followsRule = append(followsRule, val+1)
			}
		}
	}

	fmt.Println("Has to be one of these values", followsRule)
}
